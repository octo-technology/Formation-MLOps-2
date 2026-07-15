import json
import os
from pathlib import Path

import boto3
import mlflow.bedrock
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

MODEL_ID = os.getenv("MODEL_ID")

mlflow.set_experiment("agent-demo")
mlflow.bedrock.autolog()

bedrock = boto3.client("bedrock-runtime", region_name=os.environ.get("AWS_REGION"))


def get_weather(city: str) -> dict:
    """Faux outil météo, juste pour illustrer un tool call dans la trace."""
    fake_weather_db = {
        "paris": {"temperature_c": 18, "condition": "nuageux"},
        "marseille": {"temperature_c": 26, "condition": "ensoleillé"},
    }
    return fake_weather_db.get(city.lower(), {"temperature_c": 20, "condition": "inconnu"})


TOOL_CONFIG = {
    "tools": [
        {
            "toolSpec": {
                "name": "get_weather",
                "description": "Donne la météo actuelle d'une ville",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "Nom de la ville"},
                        },
                        "required": ["city"],
                    }
                },
            }
        }
    ]
}


def run_agent(question: str) -> str:
    messages = [{"role": "user", "content": [{"text": question}]}]

    # 1er appel : le modèle peut soit répondre directement, soit demander à utiliser l'outil get_weather.
    response = bedrock.converse(modelId=MODEL_ID, messages=messages, toolConfig=TOOL_CONFIG)
    output_message = response["output"]["message"]
    messages.append(output_message)

    if response["stopReason"] != "tool_use":
        return output_message["content"][0]["text"]

    # Le modèle a demandé un tool call -> on l'exécute et on renvoie le résultat.
    tool_results = []
    for block in output_message["content"]:
        if "toolUse" not in block:
            continue
        tool_use = block["toolUse"]
        city = tool_use["input"]["city"]
        weather = get_weather(city)
        tool_results.append(
            {
                "toolResult": {
                    "toolUseId": tool_use["toolUseId"],
                    "content": [{"json": weather}],
                }
            }
        )

    messages.append({"role": "user", "content": tool_results})

    # 2e appel : le modèle formule la réponse finale à partir du résultat de l'outil.
    final_response = bedrock.converse(modelId=MODEL_ID, messages=messages, toolConfig=TOOL_CONFIG)
    return final_response["output"]["message"]["content"][0]["text"]


if __name__ == "__main__":
    answer = run_agent("Quel temps fait-il à Marseille ?")
    print(json.dumps({"answer": answer}, ensure_ascii=False, indent=2))

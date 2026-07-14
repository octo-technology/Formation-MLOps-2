"""Utilitaire de diagnostic : liste les modèles Bedrock disponibles
(et les profils d'inférence) sur le compte/région configurés dans
demos/.env, pour trouver le bon `modelId` à utiliser dans integration_mlflow_agent.py.

Lancer avec :
    uv run python demos/list_bedrock_models.py
"""

import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

region = os.environ.get("AWS_REGION")
print(f"Région utilisée : {region}\n")

bedrock = boto3.client("bedrock", region_name=region)

print("=== Modèles disponibles (outputModalities=TEXT) ===")
models = bedrock.list_foundation_models(byOutputModality="TEXT")["modelSummaries"]
for m in models:
    if "anthropic" in m["modelId"] or "nova" in m["modelId"]:
        on_demand = "ON_DEMAND" in m.get("inferenceTypesSupported", [])
        print(f"- {m['modelId']:55s} on_demand={on_demand}")

print("\n=== Profils d'inférence cross-region (si le modèle direct ne marche pas) ===")
try:
    profiles = bedrock.list_inference_profiles()["inferenceProfileSummaries"]
    for p in profiles:
        if "anthropic" in p["inferenceProfileId"] or "nova" in p["inferenceProfileId"]:
            print(f"- {p['inferenceProfileId']}")
except Exception as e:
    print(f"Impossible de lister les profils d'inférence : {e}")

import pandas as pd


def monitor(latest_predictions: pd.DataFrame) -> pd.DataFrame:
    # Start filling function
    monitoring_df = pd.DataFrame({
        "predictions_time": [None],
        "predictions": [None]
    })
    # End filling function
    return monitoring_df

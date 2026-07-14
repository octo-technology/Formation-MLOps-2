import pandas as pd


def monitor(latest_predictions: pd.DataFrame) -> pd.DataFrame:
    monitoring_df = latest_predictions.groupby('predictions_time').agg({'predictions': 'mean'}).reset_index()
    return monitoring_df

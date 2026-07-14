from __future__ import annotations

import os
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd


def train_model_with_io(features_path: str, model_registry_folder: str) -> None:
    import pandas as pd

    features = pd.read_parquet(features_path)

    train_model(features, model_registry_folder)


def train_model(features: pd.DataFrame, model_registry_folder: str) -> None:
    import joblib
    import mlflow
    from sklearn.ensemble import RandomForestRegressor

    target = 'Ba_avg'
    df_x = features.drop(columns=[target])
    y = features[target]
    with mlflow.start_run():
        # log_models set to False because it doesn't work so we will log manually
        mlflow.sklearn.autolog(log_models=False)
        model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
        model.fit(df_x, y)
        mlflow.sklearn.log_model(
            sk_model=model,
            name="sklearn_model",
            registered_model_name="sklearn_model",
        )
    time_str = time.strftime('%Y%m%d-%H%M%S')
    joblib.dump(model, os.path.join(model_registry_folder, time_str + '.joblib'))


def predict_with_io(features_path: str, model_path: str, predictions_folder: str) -> None:
    import pandas as pd

    features = pd.read_parquet(features_path)
    features = predict(features, model_path)
    time_str = time.strftime('%Y%m%d-%H%M%S')
    features['predictions_time'] = time_str
    features[['predictions', 'predictions_time']].to_csv(os.path.join(predictions_folder, time_str + '.csv'),
                                                         index=False)
    features[['predictions', 'predictions_time']].to_csv(os.path.join(predictions_folder, 'latest.csv'), index=False)


def predict(features: pd.DataFrame, model_path: str) -> pd.DataFrame:
    import joblib

    model = joblib.load(model_path)
    features['predictions'] = model.predict(features)
    return features

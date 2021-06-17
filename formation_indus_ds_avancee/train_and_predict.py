import os
import time

import joblib
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def train_model_with_io(features_path: str, model_registry_folder: str) -> None:
    features = pd.read_parquet(features_path)

    train_model(features, model_registry_folder)


def train_model(features: pd.DataFrame, model_registry_folder: str) -> None:
    target = 'Ba_avg'
    X = features.drop(columns=[target])
    y = features[target]
    with mlflow.start_run() as run:
        mlflow.sklearn.autolog(log_models=True)
        model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
        model.fit(X, y)
    time_str = time.strftime('%Y%m%d-%H%M%S')
    joblib.dump(model, os.path.join(model_registry_folder, time_str + '.joblib'))


def predict_with_io(features_path: str, model_path: str, predictions_folder: str) -> None:
    features = pd.read_parquet(features_path)
    features = predict(features, model_path)
    time_str = time.strftime('%Y%m%d-%H%M%S')
    features['predictions_time'] = time_str
    features.to_csv(os.path.join(predictions_folder, time_str + '.csv'), index=False)
    features.to_csv(os.path.join(predictions_folder, 'latest.csv'), index=False)


def predict(features: pd.DataFrame, model_path: str) -> pd.DataFrame:
    model = joblib.load(model_path)
    features['predictions'] = model.predict(features)
    return features

import os

import joblib
import time
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def train_model(features_path: str, model_registry_folder: str):
    features = pd.read_parquet(features_path)

    target = 'Ba_avg'
    X = features.drop(columns=[target])
    y = features[target]

    model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
    model.fit(X, y)

    time_str = time.strftime('%Y%m%d-%H%M%S')
    joblib.dump(model, os.path.join(model_registry_folder, time_str + '.joblib'))


def predict(features_path: str, model_path: str, predictions_folder: str):
    features = pd.read_parquet(features_path)
    model = joblib.load(model_path)

    features['predictions'] = model.predict(features)
    time_str = time.strftime('%Y%m%d-%H%M%S')
    features.to_csv(os.path.join(predictions_folder, time_str + '.csv'), index=False)

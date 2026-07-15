import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def train_model(features: pd.DataFrame, model_registry_folder: str) -> None:
    target = 'Ba_avg'
    df_x = features.drop(columns=[target])
    y = features[target]
    model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
    model.fit(df_x, y)
    joblib.dump(model, os.path.join(model_registry_folder, 'model.joblib'))


def predict(features: pd.DataFrame, model_path: str) -> pd.DataFrame:
    model = joblib.load(model_path)
    features['predictions'] = model.predict(features)
    return features

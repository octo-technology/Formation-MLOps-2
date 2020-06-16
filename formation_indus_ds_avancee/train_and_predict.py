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
    joblib.dump(model, model_registry_folder + time_str + '.joblib')


def predict(features_path: str, model_path: str):
    features = pd.read_parquet(features_path)
    model = joblib.load(model_path)

    submission = model.predict(features)
    final_submit = pd.DataFrame.from_dict({'target': submission})
    final_submit.index = features.index
    final_submit.to_csv('submission.csv')

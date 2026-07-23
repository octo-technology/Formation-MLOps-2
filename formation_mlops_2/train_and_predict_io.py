import os
import time


def train_model_with_io(features_path: str, model_registry_folder: str) -> None:
    import pandas as pd

    from formation_mlops_2.train_and_predict import train_model

    features = pd.read_parquet(features_path)

    train_model(features, model_registry_folder)


def predict_with_io(features_path: str, model_path: str, predictions_folder: str) -> str:
    import pandas as pd

    from formation_mlops_2.train_and_predict import predict

    features = pd.read_parquet(features_path)
    features = predict(features, model_path)
    time_str = time.strftime('%Y%m%d-%H%M%S')
    features['predictions_time'] = time_str
    prediction_path = os.path.join(predictions_folder, time_str + '.csv')
    features[['predictions', 'predictions_time']].to_csv(prediction_path,
                                                         index=False)
    return prediction_path

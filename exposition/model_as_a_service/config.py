import os

INFERENCE_HOST = os.environ.get('INFERENCE_HOST', 'localhost')

PROJECT_FOLDER = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
PREDICTIONS_FOLDER = os.path.join(DATA_FOLDER, 'predictions')

TRAIN_DATA_PATH = os.path.join(DATA_FOLDER, 'la-haute-borne-data-2017-2020.csv')
GENERATED_DATA_PATH = os.path.join(DATA_FOLDER,
                                   'la-haute-borne-data-2017-2020.csv')  # TODO change, should point to generator

FEATURES_PATH = os.path.join(DATA_FOLDER, 'prepared_features.parquet')

MODEL_REGISTRY_FOLDER = '.'
MODEL_PATH = os.path.join(MODEL_REGISTRY_FOLDER,
                          '20260710-112838.joblib')  # To change when needed
print("MODEL_PATH:", MODEL_PATH)

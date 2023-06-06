import os

PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
PREDICTIONS_FOLDER = os.path.join(DATA_FOLDER, 'predictions')

TRAIN_DATA_PATH = os.path.join(DATA_FOLDER, 'la-haute-borne-data-2013-2016.csv')
GENERATED_DATA_PATH = os.path.join(DATA_FOLDER,
                                   'la-haute-borne-data-2013-2016.csv')  # TODO change, should point to generator

FEATURES_PATH = os.path.join(DATA_FOLDER, 'prepared_features.parquet')

MODEL_REGISTRY_FOLDER = os.path.join(PROJECT_FOLDER, 'models')
MODEL_PATH = os.path.join(MODEL_REGISTRY_FOLDER, 'model.joblib')  # To change when needed

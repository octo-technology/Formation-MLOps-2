import os

PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("PROJECT_FOLDER:", PROJECT_FOLDER)

DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
PREDICTIONS_FOLDER = '.'
print("PREDICTIONS_FOLDER:", PREDICTIONS_FOLDER)

TRAIN_DATA_PATH = os.path.join(DATA_FOLDER, 'la-haute-borne-data-2017-2020.csv')
GENERATED_DATA_PATH = os.path.join(DATA_FOLDER,
                                   'la-haute-borne-data-2017-2020.csv')  # TODO change, should point to generator

FEATURES_PATH = os.path.join(DATA_FOLDER, 'prepared_features.parquet')

MODEL_REGISTRY_FOLDER = '.'
MODEL_PATH = os.path.join(MODEL_REGISTRY_FOLDER,
                          '20200616-140746.joblib')  # To change when needed
print("MODEL_PATH:", MODEL_PATH)

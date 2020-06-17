from config import GENERATED_DATA_PATH, FEATURES_PATH, MODEL_PATH, PREDICTIONS_FOLDER
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import predict

prepare_features(GENERATED_DATA_PATH, FEATURES_PATH, training_mode=False)
predict(FEATURES_PATH, MODEL_PATH, PREDICTIONS_FOLDER)

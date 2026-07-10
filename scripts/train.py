import pandas as pd
from config import MODEL_REGISTRY_FOLDER, TRAIN_DATA_PATH

from formation_mlops_2.feature_engineering import prepare_features
from formation_mlops_2.train_and_predict import train_model

train_df = pd.read_csv(TRAIN_DATA_PATH, sep=';')
prepared_features_df = prepare_features(train_df, training_mode=True)
train_model(prepared_features_df, MODEL_REGISTRY_FOLDER)

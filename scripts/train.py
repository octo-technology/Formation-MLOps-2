import pandas as pd

from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import train_model
from config import TRAIN_DATA_PATH, MODEL_REGISTRY_FOLDER

train_df = pd.read_csv(TRAIN_DATA_PATH, sep=';')
prepared_features_df = prepare_features(train_df, training_mode=True)
train_model(prepared_features_df, MODEL_REGISTRY_FOLDER)

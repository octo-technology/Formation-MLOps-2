import pandas as pd

from config import GENERATED_DATA_PATH, MODEL_PATH
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import predict

generated_features_df = pd.read_csv(GENERATED_DATA_PATH, sep=';')
prepared_features_df = prepare_features(generated_features_df, training_mode=False)
print(predict(prepared_features_df, MODEL_PATH))

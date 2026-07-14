import os
import sys
from datetime import timedelta

import pendulum
from airflow.sdk import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import DATA_FOLDER, MODEL_REGISTRY_FOLDER, TRAIN_DATA_PATH
from formation_mlops_2.feature_engineering_io import prepare_features_with_io
from formation_mlops_2.train_and_predict_io import train_model_with_io


@dag(default_args={'owner': 'airflow'}, schedule=timedelta(weeks=4),
     start_date=pendulum.today('UTC').add(hours=-1))
def train_model():
    @task
    def prepare_features_task() -> str:
        feature_train_path: str = os.path.join(DATA_FOLDER, 'prepared_features_train.parquet')
        prepare_features_with_io(data_path=TRAIN_DATA_PATH, features_path=feature_train_path, training_mode=True)
        return feature_train_path

    @task
    def train_model_task(feature_path: str) -> None:
        train_model_with_io(features_path=feature_path, model_registry_folder=MODEL_REGISTRY_FOLDER)

    feature_path = prepare_features_task()
    train_model_task(feature_path)


train_model_dag = train_model()

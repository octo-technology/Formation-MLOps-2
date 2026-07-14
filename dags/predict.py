import os
import sys
from datetime import datetime, timedelta

import pendulum
from airflow.sdk import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import DATA_FOLDER, GENERATED_DATA_PATH, MODEL_PATH, MONITORING_TABLE_NAME, PREDICTIONS_FOLDER
from formation_mlops_2.feature_engineering_io import prepare_features_with_io
from formation_mlops_2.monitoring_io import monitor_with_io
from formation_mlops_2.train_and_predict_io import predict_with_io


@dag(default_args={'owner': 'airflow'}, schedule=timedelta(minutes=2),
     start_date=pendulum.today('UTC').add(hours=-1))
def predict():
    @task
    def prepare_features_with_io_task():
        features_path = os.path.join(DATA_FOLDER, f'prepared_features_{datetime.now()}.parquet')
        prepare_features_with_io(data_path=GENERATED_DATA_PATH,
                                 features_path=features_path,
                                 training_mode=False)
        return features_path

    @task
    def predict_with_io_task(feature_path: str) -> None:
        predict_with_io(features_path=feature_path,
                        model_path=MODEL_PATH,
                        predictions_folder=PREDICTIONS_FOLDER)

    @task
    def monitor_task():
        monitor_with_io(predictions_folder=PREDICTIONS_FOLDER,
                        monitoring_table_name=MONITORING_TABLE_NAME,
                        db_con_str='postgresql://postgres:postgres@postgres:5432/postgres')

    feature_path = prepare_features_with_io_task()
    predict_with_io_task(feature_path=feature_path)
    monitor_task()


predict_dag = predict()

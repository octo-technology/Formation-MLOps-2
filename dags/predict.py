import os
import sys
from datetime import timedelta, datetime

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from dags.config import GENERATED_DATA_PATH, DATA_FOLDER, MODEL_PATH, PREDICTIONS_FOLDER, MONITORING_TABLE_NAME
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.monitoring import monitor_with_io
from formation_indus_ds_avancee.train_and_predict import predict_with_io

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files


@dag(default_args={'owner': 'airflow'}, schedule_interval=timedelta(minutes=2), start_date=days_ago(n=0, hour=1))
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

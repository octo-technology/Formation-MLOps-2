import os
import sys
from datetime import timedelta, datetime

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from dags.config import GENERATED_DATA_PATH, DATA_FOLDER, MODEL_PATH, PREDICTIONS_FOLDER
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
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

    # Start completing predict task
    # predict = PythonOperator()
    # End completing predict task

    feature_path = prepare_features_with_io_task()
    # predict_with_io_task(feature_path=feature_path)


predict_dag = predict()

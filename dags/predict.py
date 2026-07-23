import os
import sys
from datetime import datetime, timedelta

from airflow.sdk import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import DATA_FOLDER, GENERATED_DATA_PATH, MODEL_PATH, MONITORING_TABLE_NAME, PREDICTIONS_FOLDER
from formation_mlops_2.feature_engineering_io import prepare_features_with_io
from formation_mlops_2.monitoring_io import monitor_with_io
from formation_mlops_2.train_and_predict_io import predict_with_io


# Here we use catchup=False, due to TP contexte, in other contexte either use catchup=True,
# or have your code deal with eventual missed runs
@dag(default_args={'owner': 'airflow'}, schedule=timedelta(minutes=2),
     start_date=datetime(2026, 7, 1), catchup=False)
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
        prediction_path = predict_with_io(features_path=feature_path,
                                          model_path=MODEL_PATH,
                                          predictions_folder=PREDICTIONS_FOLDER)
        return prediction_path

    @task
    def monitor_task(prediction_path: str):
        monitor_with_io(prediction_path=prediction_path,
                        monitoring_table_name=MONITORING_TABLE_NAME,
                        db_con_str='postgresql://postgres:postgres@postgres:5432/postgres')

    feature_path = prepare_features_with_io_task()
    prediction_path = predict_with_io_task(feature_path=feature_path)
    monitor_task(prediction_path=prediction_path)


predict_dag = predict()

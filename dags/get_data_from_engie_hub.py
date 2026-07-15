import os
import sys
from datetime import datetime, timedelta

from airflow.sdk import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import GENERATED_DATA_FOLDER, TRAIN_DATA_PATH
from formation_mlops_2.data_loading_io import get_data_from_csv


# Here we use catchup=False, due to TP contexte, in other contexte either use catchup=True,
# or have your code deal with eventual missed runs
@dag(default_args={'owner': 'airflow'}, schedule=timedelta(minutes=2),
     start_date=datetime(2026, 7, 1),catchup=False)
def data_generator():
    @task
    def get_data_from_csv_task():
        get_data_from_csv(train_data_path=TRAIN_DATA_PATH, data_folder=GENERATED_DATA_FOLDER)

    get_data_from_csv_task()


data_generator_dag = data_generator()

import os
import sys
from datetime import timedelta

import pendulum
from airflow.decorators import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import TRAIN_DATA_PATH, GENERATED_DATA_FOLDER
from formation_indus_ds_avancee.data_loading import get_data_from_csv


@dag(default_args={'owner': 'airflow'}, schedule=timedelta(minutes=2),
     start_date=pendulum.today('UTC').add(hours=-1))
def data_generator():
    @task
    def get_data_from_csv_task():
        get_data_from_csv(train_data_path=TRAIN_DATA_PATH, data_folder=GENERATED_DATA_FOLDER)

    get_data_from_csv_task()


data_generator_dag = data_generator()

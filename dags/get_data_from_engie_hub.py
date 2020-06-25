from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from dags.config import TRAIN_DATA_PATH, DATA_FOLDER
from formation_indus_ds_avancee.data_loading import get_data_from_csv

dag = DAG(dag_id='data_generator',
          description='Get data every 2min from Engie hub CSV',
          catchup=False,
          start_date=days_ago(1),
          schedule_interval=timedelta(minutes=2))

get_data = PythonOperator(task_id='get_data_from_csv',
                          python_callable=get_data_from_csv,
                          dag=dag,
                          provide_context=False,
                          op_kwargs={'train_data_path': TRAIN_DATA_PATH,
                                     'data_folder': DATA_FOLDER})  # TODO to change

get_data

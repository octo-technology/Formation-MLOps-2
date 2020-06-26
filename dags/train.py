import os
import sys
from datetime import timedelta

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from dags.config import TRAIN_DATA_PATH, FEATURES_PATH, MODEL_REGISTRY_FOLDER
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.train_and_predict import train_model_with_io

dag = DAG(dag_id='train',
          description='Training DAG',
          start_date=days_ago(1),
          schedule_interval=timedelta(weeks=4))

prepare_features = PythonOperator(task_id='prepare_features',
                                  python_callable=prepare_features_with_io,
                                  dag=dag,
                                  provide_context=False,
                                  op_kwargs={'data_path': TRAIN_DATA_PATH,
                                             'features_path': FEATURES_PATH,
                                             'training_mode': True})

train_model = PythonOperator(task_id='train_model',
                             python_callable=train_model_with_io,
                             dag=dag,
                             provide_context=False,
                             op_kwargs={'features_path': FEATURES_PATH,
                                        'model_registry_folder': MODEL_REGISTRY_FOLDER})

prepare_features >> train_model

import os
import sys
from datetime import timedelta

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from dags.config import MODEL_PATH, FEATURES_PATH, GENERATED_DATA_PATH, PREDICTIONS_FOLDER, MONITORING_TABLE_NAME
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.monitoring import monitor_with_io
from formation_indus_ds_avancee.train_and_predict import predict_with_io

dag = DAG(dag_id='predict',
          description='Prediction DAG',
          catchup=False,
          start_date=days_ago(1),
          schedule_interval=timedelta(minutes=15))

prepare_features = PythonOperator(task_id='prepare_features',
                                  python_callable=prepare_features_with_io,
                                  dag=dag,
                                  provide_context=False,
                                  op_kwargs={'data_path': GENERATED_DATA_PATH,
                                             'features_path': FEATURES_PATH,
                                             'training_mode': False})

predict = PythonOperator(task_id='predict',
                         python_callable=predict_with_io,
                         dag=dag,
                         provide_context=False,
                         op_kwargs={'features_path': FEATURES_PATH,
                                    'model_path': MODEL_PATH,
                                    'predictions_folder': PREDICTIONS_FOLDER})

monitor = PythonOperator(task_id='monitor',
                         python_callable=monitor_with_io,
                         dag=dag,
                         provide_context=False,
                         op_kwargs={'predictions_folder': PREDICTIONS_FOLDER,
                                    'monitoring_table_name': MONITORING_TABLE_NAME,
                                    'db_con_str': 'postgresql://postgres:postgres@postgres:5432/postgres'})

prepare_features >> predict >> monitor

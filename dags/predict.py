from datetime import timedelta

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from config import MODEL_PATH, FEATURES_PATH, GENERATED_DATA_PATH, PREDICTIONS_FOLDER
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.monitoring import monitor_with_io
from formation_indus_ds_avancee.train_and_predict import predict_with_io

dag = DAG(dag_id='predict',
          description='Prediction DAG',
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
                                    'db_con_str': 'postgresql://admin:admin@0.0.0.0:5432/monitoring'})

prepare_features >> predict >> monitor

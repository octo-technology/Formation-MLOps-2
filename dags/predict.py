from datetime import timedelta

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import predict

DATA_PATH = 'data/la-haute-borne-data-2017-2020.csv'
FEATURES_PATH = 'prepared_features.parquet'
MODEL_PATH = 'random_forest.joblib'

dag = DAG(dag_id='predict',
          description='Prediction DAG',
          start_date=days_ago(1),
          schedule_interval=timedelta(minutes=15))

prepare_features = PythonOperator(task_id='prepare_features',
                                  python_callable=prepare_features,
                                  dag=dag,
                                  provide_context=False,
                                  op_kwargs={'data_path': DATA_PATH,
                                             'features_path': FEATURES_PATH,
                                             'training_mode': False})

predict = PythonOperator(task_id='predict',
                         python_callable=predict,
                         dag=dag,
                         provide_context=False,
                         op_kwargs={'features_path': FEATURES_PATH,
                                    'model_path': MODEL_PATH})

prepare_features >> predict

from datetime import timedelta

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from config.config import DATA_PATH, FEATURES_PATH, MODEL_PREFIX, MODEL_REGISTRY_FOLDER
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import train_model

dag = DAG(dag_id='train',
          description='Training DAG',
          start_date=days_ago(1),
          schedule_interval=timedelta(weeks=4))

prepare_features = PythonOperator(task_id='prepare_features',
                                  python_callable=prepare_features,
                                  dag=dag,
                                  provide_context=False,
                                  op_kwargs={'data_path': DATA_PATH,
                                             'features_path': FEATURES_PATH})

train_model = PythonOperator(task_id='train_model',
                             python_callable=train_model,
                             dag=dag,
                             provide_context=False,
                             op_kwargs={'features_path': FEATURES_PATH,
                                        'model_registry_folder': MODEL_REGISTRY_FOLDER})

prepare_features >> train_model

from datetime import timedelta

from airflow import DAG

from tasks import prepare_features, train_model

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

DATA_PATH = 'data/la-haute-borne-data-2017-2020.csv'
FEATURES_PATH = 'features_{}'

dag = DAG(dag_id='train',
          description='Training DAG',
          start_date=days_ago(1),
          schedule_interval=timedelta(weeks=4))

prepare_features = PythonOperator(task_id='prepare_features',
                                  python_callable=prepare_features,
                                  dag=dag,
                                  provide_context=True,
                                  op_kwargs={'data_path': DATA_PATH,
                                             'features_path': FEATURES_PATH})

train_model = PythonOperator(task_id='train_model',
                             python_callable=train_model,
                             dag=dag,
                             provide_context=True)

prepare_features >> train_model

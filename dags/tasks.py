import joblib
import pandas as pd
from uuid import uuid4 as uuid
from sklearn.ensemble import RandomForestRegressor

from formation_indus_ds_avancee.feature_engineering import produce_data_features, fillna_with_previous_values, \
    fillna_with_mean, fillna_with_median, fillna_with_mean_of_last_values


def prepare_features(data_path, features_path, **context):
    # TODO: we suppose we already have the data, could use a bash operator instead
    data = pd.read_csv(data_path, sep=';')
    target = 'Ba_avg'
    data = data.dropna(subset=[target], axis=0)

    data = produce_data_features(data)
    data = data.sort_values(by='date')
    features = ['Q_avg', 'Q_min', 'Q_max', 'Q_std']
    fillna_with_previous_values(features, data)

    features = ['Va1_avg', 'Va1_min', 'Va1_max', 'Va1_std']
    fillna_with_mean(features, data)

    features = ['Va2_avg', 'Va2_min', 'Va2_max', 'Va2_std']
    fillna_with_median(features, data)

    features = ['Rs_avg', 'Rs_min', 'Rs_max', 'Rs_std', 'Rm_avg', 'Rm_min', 'Rm_max', 'Rm_std']
    fillna_with_mean_of_last_values(features, data, 30, 1)

    data = data.drop(columns=['Wind_turbine_name', 'Ba_min', 'Ba_max', 'Ba_std', 'Date_time', 'date'])
    data = data.fillna(0)

    features_unique_path = features_path.format(uuid())
    data.to_parquet(features_unique_path)
    context['task_instance'].xcom_push(key='features_key', value=features_unique_path)


def train_model(**context):
    features_unique_path = context['task_instance'].xcom_pull(key='features_key')
    features = pd.read_parquet(features_unique_path)

    target = 'Ba_avg'
    X = features.drop(columns=[target])
    y = features[target]

    model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
    model.fit(X, y)
    joblib.dump(model, 'random_forest.joblib')

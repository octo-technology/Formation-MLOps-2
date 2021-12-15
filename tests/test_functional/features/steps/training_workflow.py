import os
from unittest.mock import patch

from behave import given, when, then

from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.train_and_predict import train_model_with_io

test_data_path = './tests/test_functional/test_data/'
training_data_path = test_data_path + 'sub_eolienne_data.csv'
features_path = test_data_path + 'prepared_features.parquet'
model_registry_folder = test_data_path


@given('training data is available')
def step_impl_given(context):
    assert len(os.listdir(test_data_path)) == 1
    assert os.path.exists(training_data_path)


@when('I launch the training')
@patch('mlflow.sklearn.log_model')
def step_impl_when(context, mlflow_mock):
    prepare_features_with_io(training_data_path, features_path)
    train_model_with_io(features_path, model_registry_folder)


@then('a model is added to the model registry')
def step_impl_then(context):
    models = [f for f in os.listdir(model_registry_folder) if f.endswith('.joblib')]
    assert len(models) == 1
    os.remove(features_path)
    os.remove(model_registry_folder + models[0])

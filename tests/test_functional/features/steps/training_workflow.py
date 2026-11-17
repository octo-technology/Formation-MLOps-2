import os

from behave import given, then, when

from formation_mlops_2.feature_engineering_io import prepare_features_with_io
from formation_mlops_2.train_and_predict_io import train_model_with_io

test_data_path = './tests/test_functional/test_data/'
training_data_path = test_data_path + 'sub_eolienne_data.csv'
features_path = test_data_path + 'prepared_features.parquet'
model_registry_folder = test_data_path


@given('training data is available')
def step_impl_given(context):
    assert os.path.exists(training_data_path)
    # Start from a clean folder: remove what a previous failed run may have left
    for file_name in os.listdir(test_data_path):
        if file_name.endswith(('.parquet', '.joblib')):
            os.remove(os.path.join(test_data_path, file_name))


@when('I launch the training')
def step_impl_when(context):
    prepare_features_with_io(training_data_path, features_path)
    train_model_with_io(features_path, model_registry_folder)


@then('a model is added to the model registry')
def step_impl_then(context):
    models = [f for f in os.listdir(model_registry_folder) if f.endswith('.joblib')]
    assert len(models) == 1
    os.remove(features_path)
    os.remove(model_registry_folder + models[0])

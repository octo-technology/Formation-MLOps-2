from behave import *
import os
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import train_model

test_data_path = './tests/test_integration/test_data/'
training_data_path = test_data_path + 'sub_eolienne_data.csv'
features_path = test_data_path + 'prepared_features.parquet'
model_registry_folder = test_data_path + 'models/'


@given('training data is available')
def step_impl(context):
    assert len(os.listdir(test_data_path)) == 2
    assert os.path.exists(training_data_path)


@when('I launch the training')
def step_impl(context):
    prepare_features(training_data_path, features_path)
    train_model(features_path, model_registry_folder)


@then('a model is created in the right folder')
def step_impl(context):
    models = os.listdir(model_registry_folder)
    assert len(models) == 1
    os.remove(features_path)
    os.remove(model_registry_folder + models[0])

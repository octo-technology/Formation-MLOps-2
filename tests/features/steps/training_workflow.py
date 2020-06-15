from behave import *
import os
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import train_model

training_data_path = '../../test_data/sub_eolienne_data.csv'
features_path = '../../test_data/test_prepared_features.parquet'
model_path = '../../test_data/test_model.joblib'


@given('training data is available')
def step_impl(context):
    assert os.path.exists(training_data_path)


@when('I launch the training')
def step_impl(context):
    prepare_features(training_data_path, features_path)
    train_model(features_path, model_path)


@then('a model is created in the right folder')
def step_impl(context):
    assert os.path.exists(model_path)
    os.remove(features_path)
    os.remove(model_path)

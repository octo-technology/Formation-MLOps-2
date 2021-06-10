import os
import dags
from pytest import mark
from airflow.models import DagBag


def test_airflow_should_not_return_import_errors_when_importing_dags():
    # Given
    given_dagbag = DagBag(os.path.dirname(
        dags.__file__), include_examples=False)

    # When + Then
    assert len(given_dagbag.import_errors) == 0


def test_airflow_should_find_all_expected_dag_ids():
    # Given
    given_dagbag = DagBag(os.path.dirname(
        dags.__file__), include_examples=False)
    expected_dag_ids = {'data_generator', 'train_model', 'predict'}

    # When
    found_dags = set(given_dagbag.dag_ids)
    print(found_dags)
    # Then
    assert expected_dag_ids.issubset(found_dags)

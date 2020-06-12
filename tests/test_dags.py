import os
import unittest

from airflow.models import DagBag

import dags


class TestDagIntegrity(unittest.TestCase):
    LOAD_SECOND_THRESHOLD = 2

    def test_import_dags(self):
        # Given
        given_dagbag = DagBag(os.path.dirname(dags.__file__), include_examples=False)

        # When + then
        self.assertFalse(
            len(given_dagbag.import_errors),
            'DAG import failures. Errors: {}'.format(
                given_dagbag.import_errors
            )
        )

    def test_all_dags_found(self):
        # Given
        given_dagbag = DagBag(os.path.dirname(dags.__file__), include_examples=False)
        expected_dag_ids = {'data_generator'}

        # When
        found_dags = set(given_dagbag.dag_ids)

        # Then
        self.assertTrue(expected_dag_ids.issubset(found_dags))

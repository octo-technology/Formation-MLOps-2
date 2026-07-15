from dags.config import MONITORING_TABLE_NAME


def test_monitoring_table_name_as_been_changed():
    # Please change monitoring table name so that you don't overwrite monitoring from other attendees
    assert MONITORING_TABLE_NAME != "monitoring"

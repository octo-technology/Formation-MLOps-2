def monitor_with_io(prediction_path: str, db_con_str: str, monitoring_table_name: str) -> None:
    import pandas as pd
    from sqlalchemy import create_engine

    from formation_mlops_2.monitoring import monitor

    predictions = pd.read_csv(prediction_path,
                              usecols=['predictions_time', 'predictions'],
                              parse_dates=['predictions_time'],
                              date_parser=lambda x: pd.to_datetime(x, format='%Y%m%d-%H%M%S'))

    monitoring_df = monitor(predictions)

    engine = create_engine(db_con_str)
    db_conn = engine.connect()
    monitoring_df.to_sql(monitoring_table_name, con=db_conn, if_exists='append', index=False)
    db_conn.close()

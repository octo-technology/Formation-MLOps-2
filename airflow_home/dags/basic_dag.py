import pendulum

local_tz = pendulum.timezone('Europe/Berlin')

dag = DAG('sample_dag', description='This is a sample DAG for local timezone',
          start_date=datetime(2018, 11, 1, tzinfo=local_tz),
          schedule_interval='0 3 * * *')
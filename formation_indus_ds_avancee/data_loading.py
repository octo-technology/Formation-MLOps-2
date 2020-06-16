import datetime
import os
import pandas as pd

from config import TRAIN_DATA_PATH, DATA_FOLDER


def get_data_from_csv():
    df_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), TRAIN_DATA_PATH)
    df = pd.read_csv(df_path, sep=';')
    data1 = df.sample(n=1, random_state=1)
    data1.Date_time = datetime.datetime.now()
    data2 = df.sample(n=1, random_state=1)
    data2.Date_time = datetime.datetime.now() + datetime.timedelta(seconds=60)
    new_data = pd.concat([data1, data2], ignore_index=True)
    new_data.to_csv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), DATA_FOLDER + str(datetime.datetime.now()) + '.csv'))

import datetime
from time import sleep

import pandas as pd


def get_data_from_csv(df_path):
    df = pd.read_csv(df_path, sep=';')
    data1 = df.sample(n=1, random_state=1)
    data1.Date_time = datetime.datetime.now()
    sleep(60)
    data2 = df.sample(n=1, random_state=1)
    data2.Date_time = datetime.datetime.now()
    new_data = data1.concate(data2)
    new_data.to_csv('../../input/'+'data_'+str(datetime.datetime.now())+'.csv')


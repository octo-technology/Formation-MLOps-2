import datetime
import os
import pandas as pd


def get_data_from_csv(train_data_path: str, data_folder: str) -> None:
    df = pd.read_csv(train_data_path, sep=';')
    random_line_1 = df.sample(n=1, random_state=1)
    random_line_1.Date_time = datetime.datetime.now()
    random_line_2 = df.sample(n=1, random_state=1)
    random_line_2.Date_time = datetime.datetime.now() + datetime.timedelta(seconds=60)
    new_data = pd.concat([random_line_1, random_line_2], ignore_index=True)
    new_data.to_csv(os.path.join(data_folder, str(datetime.datetime.now()) + '.csv'), index=False, sep=";")
    new_data.to_csv(os.path.join(data_folder, 'latest.csv'), index=False, sep=";")

import pandas as pd

def produce_data_features(dataframe):
    dataframe['date']      = pd.to_datetime(dataframe.Date_time, utc=True)
    dataframe['year']      = dataframe['date'].dt.year
    dataframe['month']     = dataframe['date'].dt.month
    dataframe['season']    = dataframe['month'].apply(lambda x : get_season(x))
    return dataframe 


def get_season(month):
    return (month%12 + 3)//3 
import pandas as pd

def produce_data_features(df):
    df['date']      = pd.to_datetime(df.Date_time, utc=True)
    df['year']      = df['date'].dt.year
    df['month']     = df['date'].dt.month
    df['season']    = df['month'].apply(lambda x : get_season(x))
    df = df.drop(columns=['Date_time', 'date'])
    return df 


def get_season(month):
    return (month%12 + 3)//3 
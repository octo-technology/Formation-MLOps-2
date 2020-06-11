import pandas as pd
from typing import List


def produce_data_features(data_frame: pd.DataFrame):
    data_frame['date'] = pd.to_datetime(data_frame.Date_time, utc=True)
    data_frame['year'] = data_frame['date'].dt.year
    data_frame['month'] = data_frame['date'].dt.month
    data_frame['season'] = data_frame['month'].apply(lambda x: get_season(x))
    return data_frame


def get_season(month: int):
    return (month % 12 + 3) // 3


def fillna_with_previous_values(features: List[str], df: pd.DataFrame):
    for feature in features:
        df[feature] = df[feature].fillna(method='ffill')
    return df


def fillna_with_mean(features: List[str], df: pd.DataFrame):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].mean())
    return df


def fillna_with_median(features: List[str], df: pd.DataFrame):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())
    return df


def fillna_with_mean_of_last_values(features: List[str], df: pd.DataFrame, window: int, min_per: int):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].rolling(window, min_periods=min_per).mean())
    return df

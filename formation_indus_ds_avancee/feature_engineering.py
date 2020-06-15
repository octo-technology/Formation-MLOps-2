import pandas as pd
from typing import List


def prepare_features(data_path: str, features_path: str, training_mode=True):
    data = pd.read_csv(data_path, sep=';')

    target = 'Ba_avg'
    if training_mode:
        data = data.dropna(subset=[target], axis=0)
    else:
        data = data.drop(columns=[target], errors='ignore')

    data = produce_data_features(data)
    data = data.sort_values(by='date')
    features = ['Q_avg', 'Q_min', 'Q_max', 'Q_std']
    fillna_with_previous_values(features, data)

    features = ['Va1_avg', 'Va1_min', 'Va1_max', 'Va1_std']
    fillna_with_mean(features, data)

    features = ['Va2_avg', 'Va2_min', 'Va2_max', 'Va2_std']
    fillna_with_median(features, data)

    features = ['Rs_avg', 'Rs_min', 'Rs_max', 'Rs_std', 'Rm_avg', 'Rm_min', 'Rm_max', 'Rm_std']
    fillna_with_mean_of_last_values(features, data, 30, 1)

    data = data.drop(columns=['Wind_turbine_name', 'Ba_min', 'Ba_max', 'Ba_std', 'Date_time', 'date'])
    data = data.fillna(0)

    data.to_parquet(features_path)


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

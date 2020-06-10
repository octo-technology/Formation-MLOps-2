import pandas as pd


def produce_data_features(dataframe):
    dataframe['date'] = pd.to_datetime(dataframe.Date_time, utc=True)
    dataframe['year'] = dataframe['date'].dt.year
    dataframe['month'] = dataframe['date'].dt.month
    dataframe['season'] = dataframe['month'].apply(lambda x: get_season(x))
    return dataframe


def get_season(month):
    return (month % 12 + 3) // 3


def fillna_with_previous_values(features, df):
    for feature in features:
        df[feature] = df[feature].fillna(method='ffill')
    return df


def fillna_with_mean(features, df):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].mean())
    return df


def fillna_with_median(features, df):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())
    return df


def fillna_with_mean_of_last_values(features, df, window, min_per):
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].rolling(window,min_periods=min_per).mean())
    return df
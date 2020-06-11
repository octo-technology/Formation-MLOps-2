import pytest
import pandas as pd
import numpy as np
from formation_indus_ds_avancee.feature_engineering import produce_data_features, get_season, fillna_with_previous_values, fillna_with_mean, fillna_with_median, fillna_with_mean_of_last_values
from pandas.testing import assert_frame_equal


def test_produce_data_feature_create_feature_year_month_season():
    # given
    df = pd.read_csv("/Users/ismail.lachheb/Projects/dsin2/la-haute-borne-data-2017-2020.csv", sep=";")
    #df = pd.read_csv("/Users/lea.naccache/CODE/cercle_formation/la-haute-borne-data-2017-2020.csv", sep=";")

    # when 
    df_output = produce_data_features(df)

    # then
    assert 'date' in df_output.keys()
    assert 'month' in df_output.keys()
    assert 'season' in df_output.keys()


def test_get_season_return_the_correct_season():
    # given 
    month = 12
    season = 1

    # when 
    output_season = get_season(month)

    # then 
    assert season == output_season


def test_fillna_with_previous_values():
    # given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.1, np.nan, 0.2, 0.4]})
    df_expected = pd.DataFrame({'Q': [0.1, 0.1, 0.2, 0.4]})

    # when
    df = fillna_with_previous_values(features, df)

    # then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)


def test_fillna_with_mean_value():
    # given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4,  np.nan, 0.2, 0.4]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4]})

    # when
    df = fillna_with_mean(features, df)

    # then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)


def test_fillna_with_median_value():
    # given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4,  np.nan, 0.2, 0.4, 0.3]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4, 0.3]})

    # when
    df = fillna_with_median(features, df)

    # then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)



def test_fillna_with_mean_rolling_value():
    # given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4,  np.nan, 0.2, 0.4, 0.3]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4, 0.3]})

    # when
    df = fillna_with_mean_of_last_values(features, df, 3, 1)

    # then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)

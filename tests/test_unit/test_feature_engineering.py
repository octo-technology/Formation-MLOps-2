from datetime import datetime

import pandas as pd
import numpy as np
from formation_indus_ds_avancee.feature_engineering import create_date_features, get_season, \
    fillna_with_previous_values, fillna_with_mean, fillna_with_median, fillna_with_mean_of_last_values
from pandas.testing import assert_frame_equal


def test_create_date_features_should_create_features_year_month_season():
    # Given
    input_df = pd.DataFrame({'Date_time': [datetime(2020, 6, 21)]})

    # When
    df_output = create_date_features(input_df)

    # Then
    assert 'date' in df_output.keys()
    assert 'year' in df_output.keys()
    assert 'month' in df_output.keys()
    assert 'season' in df_output.keys()


def test_get_season_should_return_the_season_from_the_month():
    # Given
    month = 12
    season = 1

    # When
    output_season = get_season(month)

    # Then
    assert season == output_season


def test_fillna_with_previous_values_should_apply_backward_fill():
    # Given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.1, np.nan, 0.2, 0.4]})
    df_expected = pd.DataFrame({'Q': [0.1, 0.1, 0.2, 0.4]})

    # When
    df = fillna_with_previous_values(features, df)

    # Then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)


def test_fillna_with_mean_value_should_replace_na_with_column_mean():
    # Given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4, np.nan, 0.2, 0.4]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4]})

    # When
    df = fillna_with_mean(features, df)

    # Then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)


def test_fillna_with_median_value_should_replace_na_with_column_median():
    # Given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4, np.nan, 0.2, 0.4, 0.3]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4, 0.3]})

    # When
    df = fillna_with_median(features, df)

    # Then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)


def test_fillna_with_mean_rolling_value_should_replace_na_with_rolling_mean():
    # Given
    features = ['Q']
    df = pd.DataFrame({'Q': [0.2, 0.4, np.nan, 0.2, 0.4, 0.3]})
    df_expected = pd.DataFrame({'Q': [0.2, 0.4, 0.3, 0.2, 0.4, 0.3]})

    # When
    df = fillna_with_mean_of_last_values(features, df, 3, 1)

    # Then
    assert df[features].isnull().sum()[0] == 0
    assert_frame_equal(df, df_expected)

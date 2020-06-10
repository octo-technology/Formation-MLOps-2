import pytest
import pandas as pd
from src.feature_engineering import produce_data_features, get_season

def test_produce_data_feature_create_feature_year_month_season_and_remove_data_time():
    # given
    df = pd.read_csv("/Users/ismail.lachheb/Projects/dsin2/la-haute-borne-data-2017-2020.csv", sep=";")

    # when 
    df_output = produce_data_features(df)

    # then
    assert 'date' not in df_output.keys()
    assert 'month' in df_output.keys()
    assert 'season' in df_output.keys()
    assert 'Date_time' not in df_output.keys()



def test_get_season_return_the_correct_season():
    # given 
    month = 12
    season = 1

    # when 
    output_season = get_season(month)

    # then 
    assert season == output_season




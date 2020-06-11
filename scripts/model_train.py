## Imports Libraries

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import sys
from formation_indus_ds_avancee.feature_engineering import produce_data_features, fillna_with_previous_values, \
    fillna_with_mean, \
    fillna_with_median, fillna_with_mean_of_last_values

import joblib


## Load data
df = pd.read_csv(str(sys.argv[1]), sep=";")

## Feature Engineering
target = "Ba_avg"
df = df.dropna(subset=[target], axis=0)

df = produce_data_features(df)
df = df.sort_values(by='date')
features = ['Q_avg', 'Q_min', 'Q_max', 'Q_std']
fillna_with_previous_values(features, df)

features = ['Va1_avg', 'Va1_min', 'Va1_max', 'Va1_std']
fillna_with_mean(features, df)

features = ['Va2_avg', 'Va2_min', 'Va2_max', 'Va2_std']
fillna_with_median(features, df)

features = ['Rs_avg', 'Rs_min', 'Rs_max', 'Rs_std', 'Rm_avg', 'Rm_min', 'Rm_max', 'Rm_std']
fillna_with_mean_of_last_values(features, df, 30, 1)

X = df.drop(columns=["Wind_turbine_name", target, "Ba_min", "Ba_max", "Ba_std", "Date_time", "date"])
y = df[target]
X = X.fillna(0)

## Random forest model
model = RandomForestRegressor(n_estimators=1, max_depth=10, n_jobs=1)
model.fit(X, y)
joblib.dump(model, 'random_forest.joblib')

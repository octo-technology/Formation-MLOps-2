## Imports Libraries

import pandas as pd
import sys
from formation_indus_ds_avancee.feature_engineering import produce_data_features, fillna_with_previous_values, \
    fillna_with_mean, \
    fillna_with_median, fillna_with_mean_of_last_values

from joblib import load

## Load data & model
df = pd.read_csv(str(sys.argv[1]), sep=";")
model = load('random_forest.joblib')

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

## predict

submission = model.predict(X)
final_submit = pd.DataFrame.from_dict({'target': submission})
final_submit.index = df.index
final_submit.to_csv('submission.csv')

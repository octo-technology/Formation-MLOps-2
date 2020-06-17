import pandas as pd
import streamlit as st

import glob
import os

from config import PREDICTIONS_FOLDER

predictions_files = glob.glob(PREDICTIONS_FOLDER+'*.csv')
latest_predictions_file = max(predictions_files, key=os.path.getctime)
last_predictions = pd.read_csv(latest_predictions_file)

st.title('My Wind Turbine App')
st.text(latest_predictions_file)
st.dataframe(last_predictions)

st.image('https://media.giphy.com/media/rQdPpBsXTy7GU/giphy.gif')

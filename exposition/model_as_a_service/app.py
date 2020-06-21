import random
import pandas as pd
import streamlit as st
import requests

import glob
import os

from config import INFERENCE_HOST

st.title('My Wind Turbine App')
st.header('Requesting predictions to a service exposing a model')

default_wind_speed_avg = 0
received_wind_speed_avg = st.text_input(
    "Wind speed average (Ws1_avg)", default_wind_speed_avg)

if st.button('Predict with an embedded model !'):
    prediction = requests.get(
        f'http://{INFERENCE_HOST}:5000/predict?Ws1_avg={received_wind_speed_avg}').json()
    st.write('👇 Prediction with wind speed average at 👇' +
             received_wind_speed_avg)
    st.write(prediction)

st.image('https://media.giphy.com/media/rQdPpBsXTy7GU/giphy.gif',
         use_column_width=True)

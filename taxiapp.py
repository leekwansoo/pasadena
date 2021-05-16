import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title('Welcome to my studio')
    st.text('In this project I look into the transactions of taxis in NYC . ...')

with dataset: 
    st.header('NYC taxi dataset')
    st.text('I found this dataset from taxis.com, ...')
    taxi_data = pd.read_csv('taxi_data.csv')
    st.write(taxi_data.head()) 

    st.subheader('PickUp location ID Distribution')
    pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts()).head(50)
    st.bar_chart(pulocation_dist)
with features:
    st.header('The features are created')

    st.markdown('* **first feature** I created this feature...')
    st.markdown('* **second feature** I created this feature...')

with model_training:
    st.header('Time to train the model')
    st.text('The features are created')

    sel_col, disp_col = st.beta_columns(2)
    max_depth = sel_col.slider('What should be?', min_value=10, max_value=100, value=20, step=10)
    n_estimators = sel_col.selectbox('How many trees should be?', options=[100,200,300, 400], index = 0)
    input_feature = sel_col.text_input('Which feature should be?', 'PULocationID')

    regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    x = taxi_data[[input_feature]]
    y = taxi_data[['trip_distance']]

    regr.fit(x, y)
    prediction = regr.predict(y)

    disp_col.subheader('Mean absolute error of the model is:')
    disp_col.write(mean_absolute_error(y, prediction))
    disp_col.subheader('Mean squared error of the model is:')
    disp_col.write(mean_squared_error(y, prediction))
    disp_col.subheader('R squared score of the model is:')
    disp_col.write(r2_score(y, prediction))
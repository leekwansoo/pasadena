import streamlit as st
import pandas as pd 
import pandas_datareader as pdr
from datetime import datetime
from cryptocmd import CmcScraper
import plotly.express as px 

st.write('# 비트코인 BTC 데이터')

st.sidebar.header('Menu')
name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

start_date = st.sidebar.date_input('Start date', datetime(2021, 1, 1))
end_date = st.sidebar.date_input('End date', datetime(2021, 1, 7))

# https://coinmarketcap.com 
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
df = scraper.get_dataframe() 

fig_close = px.line(df, x='Date',y = ['Open', 'High', 'Low', 'Close'], title='Price')
fig_volume = px.line(df, x='Date', y = ['Volume'], title = 'Volume')
st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)
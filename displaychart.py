import streamlit as st
import numpy as np
import pandas as pd
import time
import altair as alt

df = pd.DataFrame(np.random.randn(10, 3),
    columns=('col %d' % i for i in range(3)))

st.table(df)
#chart_data = pd.DataFrame(np.random.randn(10, 3),
#    columns=['a', 'b', 'c'])
st.line_chart(df)
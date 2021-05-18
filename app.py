import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)

st.dataframe(df, 800, 400)

df = pd.DataFrame(np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)
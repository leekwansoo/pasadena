import streamlit as st

import numpy as np
import pandas as pd
import time
import altair as alt
st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

df = pd.DataFrame(np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
df = pd.DataFrame(np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.header('This is a header')

code = '''def hello(): print("Hello, Streamlit!")'''
st.code(code, language='python')
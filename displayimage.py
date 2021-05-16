import streamlit as st
import numpy as np
import pandas as pd
import time
import altair as alt
from PIL import Image

image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')

audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
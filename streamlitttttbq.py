# -*- coding: utf-8 -*-
"""streamlitttttbq.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/132cQPCN_WH3-zLwwRNsAYUbVdufKJdb2
"""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Pobierz poświadczenia z secrets
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

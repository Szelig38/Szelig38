# -*- coding: utf-8 -*-
"""Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tt8vWDZrA7nVolr8WoaBQivP_5gJkKJn
"""

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# 
# st.write('Hello, *World!* :sunglasses:')

from google.colab import drive
drive.mount('/content/drive')

!npm install localtunnel

!streamlit run app.py &>/content/logs.txt & !npx localtunnel --port 8501 & curl ipv4.icanhazip.com

!npx localtunnel --port 8501
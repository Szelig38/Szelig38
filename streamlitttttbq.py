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

# Utwórz klienta BigQuery
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT logName FROM `sst-sandbox-356409.logs.appengine_googleapis_com_nginx_health_check_20241128` LIMIT 10")

# Print results.
st.write("Przykładowe dane z naszego BQ")
for row in rows:
    st.write("✍️ " + row['logName'])

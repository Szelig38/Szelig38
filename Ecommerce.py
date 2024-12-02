import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

# Pobierz poĹ›wiadczenia z secrets
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# UtwĂłrz klienta BigQuery
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

rows = run_query("SELECT event_name FROM `johnleggy.analytics_218343504.events_20241126` LIMIT 10")

# Print results.
st.write("PrzykĹ‚adowe dane z naszego BQ")
for row in rows:
    st.write("âśŤď¸Ź " + row['event_name'])

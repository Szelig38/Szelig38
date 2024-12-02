import streamlit as st
import pandas as pd
import altair as alt
from google.oauth2 import service_account
from google.cloud import bigquery

# Ustawienia BigQuery
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    return rows

# Pobranie danych
query = """
SELECT 
    event_date, 
    event_name, 
    user_pseudo_id, 
    geo.country AS country, 
    geo.city AS city,
    purchase_revenue_in_usd,
    items.item_name AS item_name,
    items.item_revenue_in_usd AS item_revenue
FROM `analytics_218343504.events_20241128`
LIMIT 10
"""
data = run_query(query)

# Przetwarzanie danych
df = pd.DataFrame(data)
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

# Tytuł
st.title("Analiza danych e-commerce")

# Filtrowanie danych
st.sidebar.header("Filtry")
event_filter = st.sidebar.multiselect("Wybierz zdarzenia", options=df['event_name'].unique(), default=df['event_name'].unique())
country_filter = st.sidebar.multiselect("Wybierz kraj", options=df['country'].unique(), default=df['country'].unique())

filtered_data = df[(df['event_name'].isin(event_filter)) & (df['country'].isin(country_filter))]

# Sekcja analizy
st.header("Podsumowanie")
st.write(f"Liczba zdarzeń: {len(filtered_data)}")
st.write(f"Suma przychodów: {filtered_data['purchase_revenue_in_usd'].sum():,.2f} USD")

# Wykresy
st.subheader("Przychody w czasie")
revenue_chart = alt.Chart(filtered_data).mark_line().encode(
    x='event_date:T',
    y='sum(purchase_revenue_in_usd):Q',
    color='country:N'
).properties(title="Przychody w czasie")
st.altair_chart(revenue_chart, use_container_width=True)

st.subheader("Najpopularniejsze produkty")
product_chart = alt.Chart(filtered_data).mark_bar().encode(
    x='sum(item_revenue):Q',
    y=alt.Y('item_name:N', sort='-x'),
    color='item_name:N'
).properties(title="Najlepiej sprzedające się produkty")
st.altair_chart(product_chart, use_container_width=True)

# Tabela danych
st.subheader("Szczegóły zdarzeń")
st.dataframe(filtered_data)

import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(page_title="Food Order Tracking Dashboard", layout="wide")
st.title("Real-Time Food Order Tracking Dashboard")

def load_data():
    conn = sqlite3.connect("orders.db")
    df = pd.read_sql_query("""
        SELECT *
        FROM orders
        ORDER BY created_at DESC
    """, conn)
    conn.close()
    return df

placeholder = st.empty()

while True:
    df = load_data()

    with placeholder.container():
        st.subheader("Latest Orders")
        st.dataframe(df, use_container_width=True)

        if not df.empty:
            st.subheader("Metrics")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Orders", len(df))
            col2.metric("Unique Restaurants", df["restaurant_name"].nunique())
            col3.metric("Total Revenue", f"${df['amount'].sum():.2f}")

    time.sleep(5)

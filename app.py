import streamlit as st
import pandas as pd
from db import get_connection
import seed  # forces reset + seed on app start

st.set_page_config(page_title="VrijeKas — DB Debug", layout="wide")

st.title("VrijeKas — Freelance Reality Check")
st.caption("Database debug view (DataFrames only)")

conn = get_connection()

st.subheader("Variables table")
df_vars = pd.read_sql_query("SELECT * FROM variables", conn)
st.dataframe(df_vars, use_container_width=True)

st.subheader("Taxes table")
df_taxes = pd.read_sql_query("SELECT * FROM taxes", conn)
st.dataframe(df_taxes, use_container_width=True)

conn.close()

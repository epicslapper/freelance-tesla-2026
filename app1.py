import streamlit as st
import pandas as pd

from db import init_db
from calculations import calculate_summary

# --------------------------------------
# App header
# --------------------------------------

st.title("VrijeKas — Freelance Reality Check")
st.caption("Version 0.1.0")

# --------------------------------------
# Init DB (safe to call every run)
# --------------------------------------

init_db()

# --------------------------------------
# Summary
# --------------------------------------

st.header("Summary (derived, not stored)")

summary = calculate_summary()

df = pd.DataFrame(
    summary.items(),
    columns=["Metric", "Amount (€)"]
)

st.dataframe(df, use_container_width=True)

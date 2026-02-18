# db_manage.py
# Admin tool to create DB, seed it, and inspect contents

import streamlit as st
from db import init_db
from seed import seed_database
from crud import read_all

st.set_page_config(page_title="Database Management — VrijeKas", page_icon="💰")
st.title("Database Management — VrijeKas")

# Step 1: Create DB
if init_db():
    st.success("Database vrijekas.db initialized")
else:
    st.error("Database initialization failed")

# Step 2: Seed DB
seed_database()
st.success("Database seeded")

# Step 3: Display tables
st.subheader("VARIABLES")
st.dataframe(read_all("variables"))

st.subheader("BALANCE SHEET")
st.dataframe(read_all("balance_sheet"))

st.subheader("TAX STATEMENT")
st.dataframe(read_all("tax_statement"))

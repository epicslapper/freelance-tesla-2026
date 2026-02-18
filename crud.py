# crud.py
# Simple CRUD helpers for SQLite

import sqlite3
import pandas as pd

DB_NAME = "vrijekas.db"


def read_all(table_name):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    except Exception as e:
        print(f"read_all ERROR ({table_name}):", e)
        return pd.DataFrame()
    finally:
        if conn:
            conn.close()


def insert_value(table_name, name, value):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            f"INSERT OR REPLACE INTO {table_name} (name, value) VALUES (?, ?)",
            (name, value),
        )
        conn.commit()
    except Exception as e:
        print("insert_value ERROR:", e)
    finally:
        if conn:
            conn.close()

# db.py
# Database schema and creation ONLY

import sqlite3

DB_NAME = "vrijekas.db"


def init_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # ---- VARIABLES (input assumptions) ----
        c.execute("""
        CREATE TABLE IF NOT EXISTS variables (
            key TEXT PRIMARY KEY,
            value REAL NOT NULL,
            unit TEXT,
            category TEXT,
            label_nl TEXT,
            label_en TEXT,
            editable INTEGER DEFAULT 1,
            notes TEXT
        )
        """)

        # ---- DERIVED VALUES (calculation results) ----
        c.execute("""
        CREATE TABLE IF NOT EXISTS derived_values (
            key TEXT PRIMARY KEY,
            value REAL NOT NULL,
            unit TEXT,
            formula TEXT,
            notes TEXT
        )
        """)

        # ---- TAX STATEMENT (ordered fiscal logic) ----
        c.execute("""
        CREATE TABLE IF NOT EXISTS tax_statement (
            line_no INTEGER PRIMARY KEY,
            label TEXT NOT NULL,
            amount REAL NOT NULL,
            kind TEXT NOT NULL,
            notes TEXT
        )
        """)

        # ---- BALANCE SHEET (before / after snapshot) ----
        c.execute("""
        CREATE TABLE IF NOT EXISTS balance_sheet (
            item TEXT PRIMARY KEY,
            category TEXT,
            before_start REAL,
            after_1y REAL,
            notes TEXT
        )
        """)

        # ---- META (app identity & versioning) ----
        c.execute("""
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        conn.commit()
        return True

    except Exception as e:
        print("init_db ERROR:", e)
        return False

    finally:
        if conn:
            conn.close()

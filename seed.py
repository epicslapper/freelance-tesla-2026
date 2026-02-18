# seed.py
# Seed initial data into vrijekas.db
# Safe to run multiple times (INSERT OR REPLACE)

import sqlite3

DB_NAME = "vrijekas.db"


def seed_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # ----------------------------
        # VARIABLES (inputs / assumptions)
        # ----------------------------
        variables = [
            # Revenue
            ("hrs_home", 600, "hours", "revenue", "Uren thuis", "Hours home", 1, ""),
            ("rate_home", 50, "EUR/hr", "revenue", "Tarief thuis", "Hourly rate home", 1, ""),
            ("hrs_onsite", 600, "hours", "revenue", "Uren op locatie", "Hours on site", 1, ""),
            ("rate_onsite", 75, "EUR/hr", "revenue", "Tarief op locatie", "Hourly rate on site", 1, ""),

            # Car
            ("tesla_purchase_price", 50000, "EUR", "car", "Tesla aankoopprijs", "Tesla purchase price", 1, ""),
            ("vat_recovered", 8678, "EUR", "car", "Teruggevorderde BTW", "Recovered VAT", 1, ""),
            ("depreciation_years", 5, "years", "car", "Afschrijving jaren", "Depreciation years", 1, ""),

            # Tax
            ("kia_deduction", 14000, "EUR", "tax", "KIA aftrek", "KIA deduction", 1, ""),
            ("box1_tax_rate", 0.3693, "pct", "tax", "Box 1 tarief", "Box 1 tax rate", 1, ""),
            ("arbeidskorting_max", 2958, "EUR", "tax", "Max arbeidskorting", "Max labour tax credit", 1, ""),
        ]

        c.executemany("""
            INSERT OR REPLACE INTO variables
            (key, value, unit, category, label_nl, label_en, editable, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, variables)

        # ----------------------------
        # DERIVED VALUES (start empty but explicit)
        # ----------------------------
        derived_values = [
            ("total_revenue", 0.0, "EUR", "hrs_home*rate_home + hrs_onsite*rate_onsite", ""),
            ("taxable_profit", 0.0, "EUR", "see tax_statement", ""),
        ]

        c.executemany("""
            INSERT OR REPLACE INTO derived_values
            (key, value, unit, formula, notes)
            VALUES (?, ?, ?, ?, ?)
        """, derived_values)

        # ----------------------------
        # TAX STATEMENT (template lines)
        # ----------------------------
        tax_statement = [
            (10, "Total revenue", 0.0, "add", ""),
            (20, "Business expenses", 0.0, "subtract", ""),
            (30, "Bijtelling (tax-only)", 0.0, "add", ""),
            (40, "Zelfstandigenaftrek", 0.0, "subtract", ""),
            (50, "Startersaftrek", 0.0, "subtract", ""),
            (60, "MKB vrijstelling", 0.0, "subtract", ""),
            (70, "Taxable profit", 0.0, "result", ""),
            (80, "Income tax", 0.0, "tax", ""),
            (90, "Arbeidskorting", 0.0, "credit", ""),
            (100, "Final income tax", 0.0, "result", ""),
        ]

        c.executemany("""
            INSERT OR REPLACE INTO tax_statement
            (line_no, label, amount, kind, notes)
            VALUES (?, ?, ?, ?, ?)
        """, tax_statement)

        # ----------------------------
        # BALANCE SHEET (empty snapshot)
        # ----------------------------
        balance_sheet = [
            ("Cash", "asset", 0.0, 0.0, ""),
            ("Tesla (net book)", "asset", 0.0, 0.0, ""),
            ("Loan", "liability", 0.0, 0.0, ""),
            ("Equity", "equity", 0.0, 0.0, ""),
        ]

        c.executemany("""
            INSERT OR REPLACE INTO balance_sheet
            (item, category, before_start, after_1y, notes)
            VALUES (?, ?, ?, ?, ?)
        """, balance_sheet)

        # ----------------------------
        # META
        # ----------------------------
        meta = [
            ("app_name", "VrijeKas"),
            ("version", "0.1.0"),
            ("tax_year", "2026"),
        ]

        c.executemany("""
            INSERT OR REPLACE INTO meta
            (key, value)
            VALUES (?, ?)
        """, meta)

        conn.commit()
        print("Database seeded successfully.")
        return True

    except Exception as e:
        print("seed_db ERROR:", e)
        return False

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    seed_db()

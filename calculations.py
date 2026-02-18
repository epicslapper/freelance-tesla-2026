"""
calculations.py

Pure calculation layer.
- NO Streamlit
- NO printing
- NO database writes
- Reads values from SQLite
- Returns structured results (dicts)

This file assumes:
- Database already exists
- Tables are seeded
"""

from db import get_connection
from contract import *

# -------------------------------------------------
# Helpers
# -------------------------------------------------

def _read_table_as_dict(table_name: str) -> dict:
    """
    Reads a table with columns:
    var_name, value_real, value_int

    Returns:
        {
            var_name: {
                "real": value_real,
                "int": value_int
            }
        }
    """
    conn = get_connection()
    c = conn.cursor()

    c.execute(f"""
        SELECT var_name, value_real, value_int
        FROM {table_name}
    """)

    rows = c.fetchall()
    conn.close()

    result = {}
    for var_name, value_real, value_int in rows:
        result[var_name] = {
            "real": value_real,
            "int": value_int
        }

    return result


# -------------------------------------------------
# Revenue
# -------------------------------------------------

def calculate_revenue() -> dict:
    vars = _read_table_as_dict("variables")

    revenue_home = (
        vars[VAR_HOURS_HOME]["real"]
        * vars[VAR_RATE_HOME]["real"]
    )

    revenue_onsite = (
        vars[VAR_HOURS_ONSITE]["real"]
        * vars[VAR_RATE_ONSITE]["real"]
    )

    total_revenue = revenue_home + revenue_onsite

    return {
        "revenue_home": revenue_home,
        "revenue_onsite": revenue_onsite,
        "total_revenue": total_revenue
    }


# -------------------------------------------------
# Depreciation
# -------------------------------------------------

def calculate_depreciation() -> dict:
    vars = _read_table_as_dict("variables")

    base_cost = vars[VAR_TESLA_PRICE]["real"] - vars[VAR_VAT_RECOVERED]["real"]
    years = vars[VAR_DEPRECIATION_YEARS]["real"]

    annual_depreciation = base_cost / years

    return {
        "base_cost": base_cost,
        "years": years,
        "annual_depreciation": annual_depreciation
    }


# -------------------------------------------------
# Taxable Profit
# -------------------------------------------------

def calculate_taxable_profit() -> dict:
    revenue = calculate_revenue()
    depreciation = calculate_depreciation()

    taxes = _read_table_as_dict("taxes")

    profit_before_deductions = (
        revenue["total_revenue"]
        - depreciation["annual_depreciation"]
    )

    zelfstandigenaftrek = taxes[VAR_ZELFSTANDIGENAFTREK]["real"]
    startersaftrek = taxes[VAR_STARTERSAFTREK]["real"]

    profit_after_deductions = (
        profit_before_deductions
        - zelfstandigenaftrek
        - startersaftrek
    )

    mkb_pct = taxes[VAR_MKB_VRIJSTELLING_PCT]["real"]
    mkb_vrijstelling = profit_after_deductions * mkb_pct

    taxable_profit = profit_after_deductions - mkb_vrijstelling

    return {
        "profit_before_deductions": profit_before_deductions,
        "zelfstandigenaftrek": zelfstandigenaftrek,
        "startersaftrek": startersaftrek,
        "mkb_vrijstelling": mkb_vrijstelling,
        "taxable_profit": taxable_profit
    }


# -------------------------------------------------
# Income Tax
# -------------------------------------------------

def calculate_income_tax() -> dict:
    taxable = calculate_taxable_profit()
    taxes = _read_table_as_dict("taxes")

    box1_rate = taxes[VAR_BOX1_TAX_RATE]["real"]
    arbeidskorting = taxes[VAR_ARBEIDSKORTING]["real"]

    income_tax_before_credit = taxable["taxable_profit"] * box1_rate
    final_income_tax = income_tax_before_credit - arbeidskorting

    return {
        "income_tax_before_credit": income_tax_before_credit,
        "arbeidskorting": arbeidskorting,
        "final_income_tax": final_income_tax
    }


# -------------------------------------------------
# Big Picture Summary
# -------------------------------------------------

def calculate_summary() -> dict:
    revenue = calculate_revenue()
    depreciation = calculate_depreciation()
    taxable = calculate_taxable_profit()
    tax = calculate_income_tax()

    return {
        "total_revenue": revenue["total_revenue"],
        "annual_depreciation": depreciation["annual_depreciation"],
        "taxable_profit": taxable["taxable_profit"],
        "final_income_tax": tax["final_income_tax"],
        "net_cash_before_other_costs": (
            revenue["total_revenue"]
            - tax["final_income_tax"]
        )
    }

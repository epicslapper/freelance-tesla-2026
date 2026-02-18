# contract.py — VrijeKas — Freelance Reality Check
# Version 0.1.0
# Single source of truth for names of tables, variables, functions, files

# -------------------------
# Project info
# -------------------------
PROJECT_NAME = "VrijeKas — Freelance Reality Check"
PROJECT_VERSION = "0.1.0"
DATABASE_NAME = "vrijekas.db"

# -------------------------
# Files in the project
# -------------------------
FILES = [
    "app.py",
    "db.py",
    "crud.py",
    "seed.py",
    "db_delete.py",
    "db_manage.py",
    "calculations.py",
    "test_and_show_databases.py"
]

# -------------------------
# Table names
# -------------------------
TABLES = [
    "variables",
    "balance_sheet",
    "tax_statement",
    "derived_values",
    "assumptions"
]

# -------------------------
# Variable names
# -------------------------

# Revenue
VAR_HOURS_HOME = "hrs_home"
VAR_RATE_HOME = "rate_home"
VAR_HOURS_ONSITE = "hrs_onsite"
VAR_RATE_ONSITE = "rate_onsite"
VAR_TOTAL_REVENUE = "total_revenue"

# Car / Assets
VAR_TESLA_BASE_COST = "tesla_base_cost"
VAR_DEPRECIATION_YEARS = "depreciation_years"
VAR_KIA_DEDUCTION = "KIA_deduction"
VAR_CAR_OPERATIONAL_COSTS = "operational_costs"
VAR_INTEREST_PAYMENT = "interest_payment"
VAR_BIJTELLING = "bijtelling"

# Tax
VAR_BOX1_RATE = "box1_rate"
VAR_ARBEIDSKORTING = "arbeidskorting"

# -------------------------
# Function names
# -------------------------
FUNCTIONS = [
    "init_db",
    "reset_db",
    "read_table",
    "insert_variable",
    "update_variable",
    "delete_variable",
    "seed_database",
    "delete_db",
    "db_manage",
    "compute_revenue",
    "compute_car_expenses",
    "compute_taxable_profit",
    "compute_income_tax",
    "compute_net_cash",
    "run_all"
]

# -------------------------
# Pseudocode using exact names
# -------------------------

"""
# Pseudocode — Version 0.1.0

main():
    init_db()  # Create DB tables if not exist
    seed_database()  # Fill initial variables if DB empty
    parameters = read_table(TABLES[0])  # 'variables' table

    revenue_exact, revenue_rounded = compute_revenue(
        parameters[VAR_HOURS_HOME],
        parameters[VAR_RATE_HOME],
        parameters[VAR_HOURS_ONSITE],
        parameters[VAR_RATE_ONSITE]
    )

    car_exact, car_rounded = compute_car_expenses(
        parameters[VAR_TESLA_BASE_COST],
        parameters[VAR_DEPRECIATION_YEARS],
        parameters[VAR_KIA_DEDUCTION],
        parameters[VAR_CAR_OPERATIONAL_COSTS],
        parameters[VAR_INTEREST_PAYMENT]
    )

    taxable_exact, taxable_rounded = compute_taxable_profit(
        revenue_exact[VAR_TOTAL_REVENUE],
        car_exact["total_car_expenses"],
        parameters[VAR_BIJTELLING],
        parameters[VAR_KIA_DEDUCTION],
        parameters[VAR_KIA_DEDUCTION],  # Reuse placeholder for startersaftrek
        0.14  # MKB_pct example
    )

    tax_exact, tax_rounded = compute_income_tax(
        taxable_exact["taxable_profit"],
        parameters[VAR_BOX1_RATE],
        parameters[VAR_ARBEIDSKORTING]
    )

    net_cash_exact, net_cash_rounded = compute_net_cash(
        revenue_exact[VAR_TOTAL_REVENUE],
        car_exact["total_car_expenses"],
        tax_exact["final_income_tax"],
        parameters[VAR_CAR_OPERATIONAL_COSTS],
        parameters[VAR_INTEREST_PAYMENT]
    )

    display_summary(
        revenue_exact, revenue_rounded,
        car_exact, car_rounded,
        taxable_exact, taxable_rounded,
        tax_exact, tax_rounded,
        net_cash_exact, net_cash_rounded
    )
"""

# End of contract.py

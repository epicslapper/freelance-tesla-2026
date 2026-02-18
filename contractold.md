# VrijeKas — Freelance Reality Check: Meta-Contract
**Version 0.1.0**

## Meta-Metadata
This file is the **single source of truth** for the project.  
It defines all:
- filenames (.py)  
- database name  
- table names  
- column/variable names  
- function names  

All pseudocode **must use only these names**.  
All .py modules must import or parse this file to verify names.  
No name may be invented outside this file.

---

## Project
PROJECT_NAME = "VrijeKas — Freelance Reality Check"
PROJECT_VERSION = "0.1.0"
DATABASE_NAME = "vrijekas.db"

## Files
FILES = [
    "app.py",
    "db.py",
    "seed.py",
    "calculations.py",
    "test_and_show_databases.py",
]

## Tables
TABLES = [
    "variables",
    "taxes",
    "balance_items"
]

## Variables — Revenue
VAR_HOURS_HOME = "hours_home"
VAR_RATE_HOME = "rate_home"
VAR_HOURS_ONSITE = "hours_onsite"
VAR_RATE_ONSITE = "rate_onsite"
VAR_TOTAL_REVENUE = "total_revenue"

## Variables — Car / Assets
VAR_TESLA_PRICE = "tesla_price"
VAR_VAT_RECOVERED = "vat_recovered"
VAR_TESLA_BASE_COST = "tesla_base_cost"
VAR_DEPRECIATION_YEARS = "depreciation_years"
VAR_ANNUAL_DEPRECIATION = "annual_depreciation"
VAR_CAR_OPERATIONAL_COSTS = "car_operational_costs"
VAR_CAR_INTEREST_COSTS = "car_interest_costs"
VAR_BIJTELLING_TAX = "bijtelling_tax"

## Variables — Tax deductions
VAR_ZELFSTANDIGENAFTREK = "zelfstandigenaftrek"
VAR_STARTERSAFTREK = "startersaftrek"
VAR_MKB_VRIJSTELLING_PCT = "mkb_vrijstelling_pct"

## Variables — Tax parameters
VAR_BOX1_TAX_RATE = "box1_tax_rate"
VAR_ARBEIDSKORTING = "arbeidskorting"

## Functions
FUNCTIONS = [
    "init_db",
    "reset_database",
    "read_parameters",
    "update_parameter",
    "calculate_revenue",
    "calculate_expenses",
    "calculate_tax",
    "summary_dict",
]

## Pseudocode

main():
init_db()
seed_database_if_needed()
parameters = read_parameters()

revenue = calculate_revenue(parameters)
expenses = calculate_expenses(parameters)
taxes = calculate_tax(parameters)

summary = summary_dict(revenue, expenses, taxes)
display(summary)


---

This file can now be **parsed by Python** to check:  
- Are all variable names used in `.py` files listed here? ✅  
- Are all function names consistent? ✅  
- Are all table names used in SQL consistent? ✅  

---

If you approve this format, the **next step** is:

1. I will convert **`contract.md` → importable Python object**,  
   so every `.py` file can do:

```python
from contract import CONTRACT
print(CONTRACT['TABLES'])

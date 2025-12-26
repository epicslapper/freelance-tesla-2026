import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="NL Freelancer + Tesla Tax Playground", layout="wide")

st.title("🇳🇱 Freelancer 2026 – Tesla Model Y Tax Playground")

st.markdown("""
This tool explores **ballpark outcomes** for a Dutch freelancer using a **Tesla Model Y**
as a business asset.  
It focuses on **net cash**, not accounting perfection.

> Assumptions are simplified on purpose.
""")

# =========================
# INPUT PARAMETERS
# =========================
st.header("1️⃣ Input parameters")

col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = st.slider("Total revenue (€)", 40_000, 80_000, 75_000, step=1_000)
    tax_rate = st.number_input("Income tax rate (%)", value=17.8) / 100
    arbeidskorting = st.number_input("Arbeidskorting (€)", value=3_000)

with col2:
    tesla_price = st.number_input("Tesla Model Y purchase price (€)", value=50_000)
    vat_recovered = st.number_input("VAT recovered (€)", value=8_678)
    kia_deduction = st.number_input("KIA deduction (€)", value=14_000)
    depreciation_years = st.number_input("Depreciation years", value=5)

with col3:
    operational_costs = st.number_input(
        "Operational car costs per year (€)",
        value=3_000,
        help="Charging, insurance, road tax"
    )
    interest_rate = st.number_input("IBKR loan interest (%)", value=5.0) / 100
    bijtelling = st.number_input("Bijtelling (€)", value=7_291)

# =========================
# CALCULATIONS
# =========================
tesla_base_cost = tesla_price - vat_recovered
annual_depreciation = tesla_base_cost / depreciation_years
interest_cost = tesla_base_cost * interest_rate

total_car_expenses = (
    annual_depreciation
    + kia_deduction
    + operational_costs
    + interest_cost
)

taxable_profit_before_deductions = total_revenue - total_car_expenses + bijtelling

zelfstandigenaftrek = 7_280
startersaftrek = 2_123
mkb_vrijstelling = 6_067

taxable_profit_after_deductions = max(
    taxable_profit_before_deductions
    - zelfstandigenaftrek
    - startersaftrek
    - mkb_vrijstelling,
    0
)

tax_before_korting = taxable_profit_after_deductions * tax_rate
tax_after_korting = max(tax_before_korting - arbeidskorting, 0)

net_cash = (
    total_revenue
    - total_car_expenses
    - tax_after_korting
)

# =========================
# RESULTS TABLE
# =========================
st.header("2️⃣ Results")

results = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Car Expenses",
        "Taxable Profit (after deductions)",
        "Income Tax (after arbeidskorting)",
        "Net Cash"
    ],
    "€": [
        total_revenue,
        total_car_expenses,
        taxable_profit_after_deductions,
        tax_after_korting,
        net_cash
    ]
})

st.dataframe(results.style.format({"€": "€{:,.0f}"}), use_container_width=True)

# =========================
# BIG PICTURE NARRATIVE
# =========================
st.header("3️⃣ Big picture interpretation")

st.markdown(f"""
### What this shows

- You generate **€{total_revenue:,.0f}** in freelance revenue  
- The Tesla absorbs a **large chunk of taxable profit** via:
  - depreciation  
  - KIA  
  - interest  
  - operating costs  
- **Arbeidskorting bites last**, directly reducing tax payable  
- Result: **very low effective tax pressure**

### Net outcome

> **Net cash ≈ €{net_cash:,.0f}**

This ignores:
- AOW income (which stacks on top)
- Portfolio growth
- Optional emigration later

This is why the setup works **only in a narrow window**.
""")

# =========================
# REVENUE SENSITIVITY GRAPH
# =========================
st.header("4️⃣ Revenue vs Net Cash")

revenues = np.arange(40_000, 80_001, 1_000)
net_cash_list = []

for r in revenues:
    tp = r - total_car_expenses + bijtelling
    tp_after = max(tp - zelfstandigenaftrek - startersaftrek - mkb_vrijstelling, 0)
    tax = max(tp_after * tax_rate - arbeidskorting, 0)
    net_cash_list.append(r - total_car_expenses - tax)

fig, ax = plt.subplots()
ax.plot(revenues, net_cash_list)
ax.set_xlabel("Revenue (€)")
ax.set_ylabel("Net Cash (€)")
ax.set_title("Net Cash vs Revenue (Tesla included)")
ax.grid(True)

st.pyplot(fig)

# =========================
# FOOTNOTE
# =========================
st.caption("""
⚠️ Not tax advice.  
Assumes eligibility for all deductions and ignores edge cases.
""")


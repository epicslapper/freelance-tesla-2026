import streamlit as st

import pandas as pd

st.set_page_config(page_title="ZZP Tesla Tax Model", layout="wide")

st.title("ZZP Tesla – Spreadsheet Style Tax & Cashflow Model")

st.markdown("""
This app mirrors the **Excel-style calculation**, step by step.
All assumptions are explicit.  
Nothing is hidden. Change inputs at the top and read the story below.
""")

# ======================================================
# INPUT PARAMETERS (Spreadsheet style)
# ======================================================

st.header("1️⃣ Revenue assumptions")

col1, col2 = st.columns(2)

with col1:
    hours_location = st.number_input("Hours on location (hr)", value=600)
    rate_location = st.number_input("Rate on location (€ / hr)", value=75)

with col2:
    hours_home = st.number_input("Hours home office (hr)", value=600)
    rate_home = st.number_input("Rate home office (€ / hr)", value=50)

revenue_location = hours_location * rate_location
revenue_home = hours_home * rate_home
total_revenue = revenue_location + revenue_home

st.subheader("Revenue calculation")
st.write(f"Revenue on location: €{revenue_location:,.0f}")
st.write(f"Revenue home office: €{revenue_home:,.0f}")
st.write(f"**Total Revenue:** €{total_revenue:,.0f}")

st.divider()

# ======================================================
# CAR ASSUMPTIONS
# ======================================================

st.header("2️⃣ Tesla assumptions")

col1, col2 = st.columns(2)

with col1:
    tesla_purchase_price = st.number_input("Tesla Model Y purchase (€)", value=50000)
    vat_recovered = st.number_input("VAT recovered (€)", value=8678)
    depreciation_years = st.number_input("Depreciation period (years)", value=5)

with col2:
    kia_deduction = st.number_input("KIA deduction (€)", value=14000)
    operational_costs = st.number_input("Operational costs Tesla (€ / yr)", value=3000)
    interest_payment = st.number_input("Interest payment IBKR loan (€ / yr)", value=2066)

tesla_base_cost = tesla_purchase_price - vat_recovered
depreciation = tesla_base_cost / depreciation_years

total_car_expenses = depreciation + kia_deduction + operational_costs

st.subheader("Tesla cost breakdown")
st.write(f"Tesla base cost (ex VAT): €{tesla_base_cost:,.0f}")
st.write(f"Depreciation per year: €{depreciation:,.0f}")
st.write(f"KIA deduction: €{kia_deduction:,.0f}")
st.write(f"Operational costs: €{operational_costs:,.0f}")
st.write(f"**Total car expenses:** €{total_car_expenses:,.0f}")

st.divider()

# ======================================================
# BIJTELLING
# ======================================================

st.header("3️⃣ Private use & bijtelling")

private_km = st.number_input("Private use km", value=6000)
bijtelling_percentage = st.number_input("Bijtelling % (effective)", value=16.0)

bijtelling_value = tesla_base_cost * (bijtelling_percentage / 100)

st.write(f"Bijtelling (taxable): €{bijtelling_value:,.0f}")

st.divider()

# ======================================================
# TAXABLE PROFIT
# ======================================================

st.header("4️⃣ Taxable profit before deductions")

taxable_profit_before = total_revenue - total_car_expenses + bijtelling_value

st.write(f"Revenue: €{total_revenue:,.0f}")
st.write(f"Minus car expenses: €{total_car_expenses:,.0f}")
st.write(f"Plus bijtelling: €{bijtelling_value:,.0f}")
st.write(f"**Taxable profit before deductions:** €{taxable_profit_before:,.0f}")

st.divider()

# ======================================================
# DEDUCTIONS
# ======================================================

st.header("5️⃣ Entrepreneur deductions")

col1, col2 = st.columns(2)

with col1:
    zelfstandigenaftrek = st.number_input("Zelfstandigenaftrek (€)", value=7280)
    startersaftrek = st.number_input("Startersaftrek (€)", value=2123)

with col2:
    mkb_vrijstelling = st.number_input("MKB winstvrijstelling (€)", value=6067)

profit_after_deductions = taxable_profit_before - zelfstandigenaftrek - startersaftrek
taxable_profit_after = profit_after_deductions - mkb_vrijstelling

st.write(f"Profit after zelfstandigenaftrek & startersaftrek: €{profit_after_deductions:,.0f}")
st.write(f"**Taxable profit after all deductions:** €{taxable_profit_after:,.0f}")

st.divider()

# ======================================================
# TAX & ARBEIDSKORTING
# ======================================================

st.header("6️⃣ Income tax & arbeidskorting")

income_tax_rate = st.number_input("Income tax rate (%)", value=17.8)
arbeidskorting = st.number_input("Arbeidskorting (€)", value=2958)

income_tax_before = taxable_profit_after * (income_tax_rate / 100)
income_tax_after = max(income_tax_before - arbeidskorting, 0)

st.write(f"Income tax before arbeidskorting: €{income_tax_before:,.0f}")
st.write(f"Arbeidskorting: €{arbeidskorting:,.0f}")
st.write(f"**Income tax after arbeidskorting:** €{income_tax_after:,.0f}")

st.divider()

# ======================================================
# NET CASH
# ======================================================

st.header("7️⃣ Net cash position")

net_cash_before = total_revenue - total_car_expenses - income_tax_after
net_cash_final = net_cash_before - operational_costs - interest_payment

st.write(f"Net cash before ops & interest: €{net_cash_before:,.0f}")
st.write(f"Operational costs: €{operational_costs:,.0f}")
st.write(f"Interest payments: €{interest_payment:,.0f}")

st.subheader(f"✅ **Final Net Cash: €{net_cash_final:,.0f}**")

st.divider()

# ======================================================
# NARRATIVE
# ======================================================

st.header("📘 Big picture summary")

st.markdown(f"""
- Revenue is driven by **hours × rate** (location vs home office).
- The Tesla is financed **without selling assets**, interest is deductible.
- VAT is recovered upfront, lowering the true capital base.
- Depreciation + KIA do the heavy lifting early.
- Bijtelling increases taxable profit but does **not** affect cash.
- Arbeidskorting is deducted from **tax payable**, not from income.
- Result: extremely low effective tax pressure and strong net cash.
""")

st.header("8️⃣ Sanity check table (Excel-style)")

sanity_data = {
    "Item": [
        "Revenue – location",
        "Revenue – home office",
        "Total revenue",
        "Tesla base cost (ex VAT)",
        "Depreciation (annual)",
        "KIA deduction",
        "Operational costs",
        "Total car expenses",
        "Bijtelling (taxable)",
        "Taxable profit before deductions",
        "Zelfstandigenaftrek",
        "Startersaftrek",
        "MKB winstvrijstelling",
        "Taxable profit after all deductions",
        "Income tax after arbeidskorting",
        "Final net cash"
    ],
    "Amount (€)": [
        revenue_location,
        revenue_home,
        total_revenue,
        tesla_base_cost,
        depreciation,
        kia_deduction,
        operational_costs,
        total_car_expenses,
        bijtelling_value,
        taxable_profit_before,
        zelfstandigenaftrek,
        startersaftrek,
        mkb_vrijstelling,
        taxable_profit_after,
        income_tax_after,
        net_cash_final
    ]
}

st.dataframe(sanity_data, use_container_width=True)



bs_before_assets = pd.DataFrame({
    "Assets": [
        "Cash",
        "Investments (IBKR)",
        "Car",
        "Total Assets"
    ],
    "EUR": [
        10_000,
        200_000,
        0,
        210_000
    ]
})

bs_before_liabilities = pd.DataFrame({
    "Liabilities & Equity": [
        "Loan",
        "Equity",
        "Total Liabilities & Equity"
    ],
    "EUR": [
        0,
        210_000,
        210_000
    ]
})

st.subheader("Balance Sheet – BEFORE start")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Assets")
    st.table(bs_before_assets)

with col2:
    st.markdown("### Liabilities & Equity")
    st.table(bs_before_liabilities)




bs_after_assets = pd.DataFrame({
    "Assets": [
        "Cash",
        "Tesla Model Y (net book value)",
        "Investments (IBKR)",
        "Total Assets"
    ],
    "EUR": [
        72_350,
        33_058,  # 41,322 – 8,264 depreciation
        200_000,
        305_408
    ]
})

bs_after_liabilities = pd.DataFrame({
    "Liabilities & Equity": [
        "IBKR Loan",
        "Equity",
        "Total Liabilities & Equity"
    ],
    "EUR": [
        41_322,
        264_086,
        305_408
    ]
})

st.subheader("Balance Sheet – AFTER 1 year")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Assets")
    st.table(bs_after_assets)

with col2:
    st.markdown("### Liabilities & Equity")
    st.table(bs_after_liabilities)

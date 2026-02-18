from db import read_parameters

def get_parameters_dict():
    """Return parameters as a dict for easy calculation."""
    params_list = read_parameters()
    params = {p["var_name"]: p["value"] for p in params_list}
    return params

def calculate_revenue(params):
    revenue_home = params["Hours home"] * params["Rate home"]
    revenue_onsite = params["Hours onsite"] * params["Rate onsite"]
    total_revenue = revenue_home + revenue_onsite
    return {
        "revenue_home": revenue_home,
        "revenue_onsite": revenue_onsite,
        "total_revenue": total_revenue
    }

def calculate_expenses(params):
    depreciation = params["Tesla price"] / params["Depreciation years"]
    operational_costs = 3000  # Example
    interest = 2066           # Example
    total_expenses = depreciation + operational_costs + interest
    return {
        "depreciation": depreciation,
        "operational_costs": operational_costs,
        "interest": interest,
        "total_expenses": total_expenses
    }

def calculate_tax(params, total_revenue, total_expenses):
    taxable_profit = total_revenue - total_expenses + params["Bijtelling"]
    deductions = params["Self-employed deduction"] + params["Starter deduction"] + params["MKB %"]*taxable_profit
    taxable_after_deductions = taxable_profit - deductions
    income_tax = taxable_after_deductions * params["Box 1 rate"]
    final_tax = income_tax - params["Labour tax credit"]
    if final_tax < 0:
        final_tax = 0
    return {
        "taxable_profit": taxable_profit,
        "deductions": deductions,
        "taxable_after_deductions": taxable_after_deductions,
        "income_tax": income_tax,
        "final_tax": final_tax
    }

def calculate_net_cash(total_revenue, final_tax, expenses):
    net_cash = total_revenue - final_tax - expenses["operational_costs"] - expenses["interest"]
    return net_cash

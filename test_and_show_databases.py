import pandas as pd
from db import init_db, read_variables, read_taxes, read_balance_items

def rows_to_df(rows):
    return pd.DataFrame([dict(r) for r in rows])

def main():
    init_db()

    print("\n=== VARIABLES ===")
    df_vars = rows_to_df(read_variables())
    print(df_vars)

    print("\n=== TAXES ===")
    df_taxes = rows_to_df(read_taxes())
    print(df_taxes)

    print("\n=== BALANCE ITEMS ===")
    df_balance = rows_to_df(read_balance_items())
    print(df_balance)

if __name__ == "__main__":
    main()

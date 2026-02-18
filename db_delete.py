import sqlite3
import os
from config import read_config, write_config


def delete_db():
    if os.path.exists("vrijekas.db"):
        os.remove("vrijekas.db")
        print("Database file deleted.")
    else:
        print("Database file not found, nothing to delete.")

    config = read_config()
    config['db_created'] = False
    config['db_filled'] = False
    write_config(config)
    print("Config flags reset.")

import sqlite3
import pandas as pd
import os

"""
Utils for the management of the clients database.
"""

def fetch_customer():
    # Obtenir le chemin absolu de la base de données
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'banking_data.db')
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()
    return df

if __name__ == "__main__":
    print(fetch_customer())
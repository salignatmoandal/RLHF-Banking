import sqlite3
import pandas as pd
import os

"""
Utils for the management of the clients database.
"""

def fetch_customer():
    """Get all customers from database."""
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'data',
        'banking_data.db'
    )
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()
    return df

def get_customer_data(customer_id: int) -> tuple:
    """Get specific customer data from database."""
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'data',
        'banking_data.db'
    )
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT nom, prenom, credit_score, revenu_annuel FROM customers WHERE id = ?",
        (customer_id,)
    )
    result = cursor.fetchone()
    conn.close()
    return result

if __name__ == "__main__":
    print(fetch_customer())
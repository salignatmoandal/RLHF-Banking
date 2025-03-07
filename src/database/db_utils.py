import sqlite3
import pandas as pd

def fetch_customer():
    conn = sqlite3.connect('data/banking_data.db')
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()
    return df

if __name__ == "__main__":
    print(fetch_customer())
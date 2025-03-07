import sqlite3
import pandas as pd
import os

"""
Script to view the content of the clients database.
"""
# Relative path from src/database to data/banking_data.db
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'banking_data.db')

try:
    # Establish the connection to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Retrieve the customer data
    query = "SELECT * FROM customers"
    df = pd.read_sql_query(query, conn)

    # Display the data
    print(df)

except sqlite3.Error as e:
    print(f"Error when connecting to the database: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    if 'conn' in locals():
        conn.close() 
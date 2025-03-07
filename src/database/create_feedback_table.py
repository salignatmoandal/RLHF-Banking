"""
Script to create the feedback table for collecting user interactions and ratings.
"""
import os
import sqlite3

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'data',
    'banking_data.db'
)

def create_feedback_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        question TEXT,
        response TEXT,
        rating INTEGER CHECK(rating >= 1 AND rating <= 5),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        selected_policies TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_feedback_table()
    print("Feedback table created successfully!") 
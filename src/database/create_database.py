"""
Script to create and initialize the banking database with test data.
"""
import os
import sqlite3

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'data',
    'banking_data.db'
)

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    credit_score INTEGER,
    revenu_annuel FLOAT
)
''')

TEST_DATA = [
    (1, 'Dupont', 'Jean', 720, 60000),
    (2, 'Martin', 'Sophie', 680, 55000),
    (3, 'Bernard', 'Pierre', 750, 75000),
    (4, 'Durand', 'Marie', 650, 45000),
    (5, 'Lefevre', 'Luc', 700, 50000),
    (6, 'Girard', 'Sophie', 670, 52000),
    (7, 'Dubois', 'Pierre', 730, 65000),
    (8, 'Moreau', 'Marie', 660, 48000),
    (9, 'Girard', 'Luc', 710, 51000)
]

cursor.executemany('INSERT OR REPLACE INTO customers VALUES (?,?,?,?,?)', TEST_DATA)
conn.commit()
conn.close()

print("Database created successfully!") 
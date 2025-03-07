import sqlite3
import pandas as pd
import os

# Chemin vers la base de données
db_path = os.path.join('data', 'banking_data.db')

try:
    # Établir la connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Récupérer les données client
    query = "SELECT * FROM customers"
    df = pd.read_sql_query(query, conn)

    # Afficher les données
    print(df)

except sqlite3.Error as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
finally:
    # Fermer la connexion
    if 'conn' in locals():
        conn.close() 
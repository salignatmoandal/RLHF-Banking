import sqlite3
import os

# Obtenir le chemin absolu de la base de données
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'banking_data.db')

# Créer le répertoire data s'il n'existe pas
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Créer la connexion à la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Créer la table customers
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    credit_score INTEGER,
    revenu_annuel FLOAT
)
''')

# Insérer quelques données de test
test_data = [
    (1, 'Dupont', 'Jean', 720, 60000),
    (2, 'Martin', 'Sophie', 680, 55000),
    (3, 'Bernard', 'Pierre', 750, 75000),
    (4, 'Durand', 'Marie', 650, 45000),
    (5, 'Lefevre', 'Luc', 700, 50000),
    (6, 'Girard', 'Sophie', 670, 52000),
    (7, 'Dubois', 'Pierre', 730, 65000),
    (8, 'Moreau', 'Marie', 660, 48000),
    (9, 'Girard', 'Luc', 710, 51000),
    
]

cursor.executemany('INSERT OR REPLACE INTO customers VALUES (?,?,?,?,?)', test_data)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("Base de données créée avec succès!") 
import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def read_policy_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Chemin vers le répertoire des politiques
policy_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'policy_docs')

# Lire les fichiers de politique
policy_files = [
    os.path.join(policy_dir, 'loan_policy_1.txt'),
    os.path.join(policy_dir, 'loan_policy_2.txt')
]

# Charger le contenu des politiques
loan_policies = [read_policy_file(file) for file in policy_files]

# Créer et persister le vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(loan_policies, embeddings, persist_directory="data/policy_docs")
vectorstore.persist()

print("Policy documents indexed successfully.")

if __name__ == "__main__":
    print("Policies loaded:")
    for policy in loan_policies:
        print("\n---\n")
        print(policy)
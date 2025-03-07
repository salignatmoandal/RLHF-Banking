import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def read_policy_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Path to the policy directory
policy_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'policy_docs')

# Read the policy files
policy_files = [
    os.path.join(policy_dir, 'loan_policy_1.txt'),
    os.path.join(policy_dir, 'loan_policy_2.txt')
]

# Load the policy content
loan_policies = [read_policy_file(file) for file in policy_files]

# Create and persist the vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(loan_policies, embeddings, persist_directory="data/policy_docs")
vectorstore.persist()

print("Policy documents indexed successfully.")

if __name__ == "__main__":
    print("Policies loaded:")
    for policy in loan_policies:
        print("\n---\n")
        print(policy)
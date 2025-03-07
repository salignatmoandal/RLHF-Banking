import sqlite3
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

"""
Script to generate a response to a question based on the policies and the client profile.
"""

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialization of the model
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Initialisation du vectorstore avec k=2
vectorstore = Chroma(persist_directory="data/policy_docs", embedding_function=OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def get_customer_data(customer_id):
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'banking_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT nom, prenom, credit_score, revenu_annuel FROM customers WHERE id = ?", (customer_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def generate_response(customer_id, query):
    # Retrieve the customer information
    customer = get_customer_data(customer_id)
    if not customer:
        return "Client not found."
    
    nom, prenom, credit_score, revenu_annuel = customer
    
    # Récupérer les politiques pertinentes
    docs = retriever.invoke(query)
    policies = "\n".join([doc.page_content for doc in docs])
    
    # Create the prompt with the complete context
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a banking assistant. Analyze the eligibility of the client based on the policies and their profile.

Loan policies :
{policies}

Profil du client :
- Nom : {nom} {prenom}
- Score de crédit : {credit_score}
- Revenu annuel : {revenu_annuel}€

Respond to the question taking into account the policies and the client profile."""),
        ("human", "{question}")
    ])
    
    # Générer la réponse
    chain = prompt | llm
    response = chain.invoke({
        "policies": policies,
        "nom": nom,
        "prenom": prenom,
        "credit_score": credit_score,
        "revenu_annuel": revenu_annuel,
        "question": query
    })
    
    return response.content

if __name__ == "__main__":
    print(generate_response(4, "Suis-je éligible pour un prêt à faible taux d'intérêt ?"))
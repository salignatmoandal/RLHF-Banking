"""
Script to generate a response to a question based on the policies and the client profile.
"""
import os
import sqlite3
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialization of the model
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Initialization of the vectorstore with k=2
vectorstore = Chroma(
    persist_directory="data/policy_docs",
    embedding_function=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def get_customer_data(customer_id):
    """Get customer data from the database."""
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

def generate_response(customer_id, query):
    """Generate a response based on customer data and policies."""
    customer = get_customer_data(customer_id)
    if not customer:
        return "Client not found."
    
    nom, prenom, credit_score, revenu_annuel = customer
    
    docs = retriever.invoke(query)
    policies = "\n".join([doc.page_content for doc in docs])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a banking assistant. Analyze the client's eligibility based on the policies and their profile.

Loan policies:
{policies}

Client profile:
- Name: {nom} {prenom}
- Credit score: {credit_score}
- Annual income: {revenu_annuel}€

Answer the question considering both policies and client profile."""),
        ("human", "{question}")
    ])
    
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
    print(generate_response(1, "Am I eligible for a low-interest loan?"))
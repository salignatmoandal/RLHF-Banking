import sqlite3
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialisation du modèle
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Initialisation du vectorstore
vectorstore = Chroma(persist_directory="data/policy_docs", embedding_function=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

def get_customer_data(customer_id):
    conn = sqlite3.connect('data/banking_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nom, prenom, credit_score, revenu_annuel FROM customers WHERE id = ?", (customer_id,))
    result = cursor.fetchone()
    conn.close()

    return result if result else "Customer not found"

def generate_response(customer_id, query):
    # Récupérer les documents pertinents
    docs = retriever.invoke(query)
    
    # Créer le contexte
    context = "\n".join([doc.page_content for doc in docs])
    
    # Créer le prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful banking assistant. Use the following context to answer the question: {context}"),
        ("human", "{question}")
    ])
    
    # Générer la réponse
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "question": query
    })
    
    return response.content

if __name__ == "__main__":
    print(generate_response(1, "Am I eligible for a low-interest loan?"))



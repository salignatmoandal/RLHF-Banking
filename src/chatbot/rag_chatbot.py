"""
Script to generate a response to a question based on the policies and the client profile.
"""
import os
import sqlite3
import sys
from pathlib import Path

# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from feedback.feedback_collector import FeedbackCollector
from database.db_utils import get_customer_data

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize components
llm = ChatOpenAI(model="gpt-4", temperature=0)
feedback_collector = FeedbackCollector()
vectorstore = Chroma(
    persist_directory="data/policy_docs",
    embedding_function=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def generate_response(customer_id, query, collect_feedback=True):
    """Generate a response and optionally collect feedback."""
    customer = get_customer_data(customer_id)
    if not customer:
        return "Client not found."
    
    nom, prenom, credit_score, revenu_annuel = customer
    
    # Get relevant policies
    docs = retriever.invoke(query)
    selected_policies = [doc.page_content for doc in docs]
    policies = "\n".join(selected_policies)
    
    # Generate response
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
    
    response_content = response.content
    print("\nChatbot response:")
    print("-" * 50)
    print(response_content)
    print("-" * 50 + "\n")
    
    if collect_feedback:
        rating = input("Please rate the response (1-5): ")
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                feedback_collector.save_feedback(
                    customer_id=customer_id,
                    question=query,
                    response=response_content,
                    rating=rating,
                    selected_policies=selected_policies
                )
        except ValueError:
            print("Invalid rating provided")
    
    return response_content

if __name__ == "__main__":
    customer_id = int(input("Enter the customer ID: "))
    question = input("Enter your question: ")
    generate_response(customer_id, question)
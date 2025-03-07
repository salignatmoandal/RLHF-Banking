# RAG-Banking-Chatbot
The RAG-Banking-Chatbot is an AI-powered chatbot designed to provide personalized financial assistance by combining structured and unstructured data. It leverages Retrieval-Augmented Generation (RAG) to improve the accuracy of responses by fetching relevant financial policies and customer-specific details before generating an answer.

# Features
Customer Data Retrieval – Uses an SQLite database to store and fetch structured financial data.
- Policy Document Search – Utilizes ChromaDB to store and retrieve unstructured financial policies.
- Retrieval-Augmented Generation (RAG) – Enhances chatbot responses by combining retrieved information with LLM-generated text.
- Retrieval-Augmented Generation (RAG) – Enhances chatbot responses by combining retrieved information with LLM-generated text.
- Personalized Banking Advice – Tailors responses based on customer details.
- Logging & Debugging – Tracks chatbot interactions and retrieval performance.
- Scalable Architecture – Modular design for easy integration and expansion.
- Unit & Integration Testing – Ensures reliability and correctness.
- Dockerized Deployment – Supports containerized execution for portability.

# Setup & Installation
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```






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

# Initialize the Database
```
python src/database/setup_database.py
```

#Index Loan Policies in ChromaDB
```
python src/retrieval/index_policies.py
```

# Run the Chatbot
```
python src/chatbot/rag_chatbot.py
```

# How It Works
1. User asks a financial question (e.g., "Am I eligible for a low-interest loan?")
2. Chatbot retrieves customer financial data from the SQLite database.
3. Relevant financial policies are fetched from ChromaDB.
4. A Retrieval-Augmented Prompt is generated, combining retrieved information with the user query.
5. LLM processes the prompt and generates a response.
6. The chatbot returns a factual, personalized answer.


# Technologies Used
- Python (Primary programming language)
- SQLite (Structured data storage)
- ChromaDB (Vector database for unstructured data retrieval)
- LangChain (LLM and retrieval integration)
- OpenAI GPT API (Language model for response generation)
- Docker (Containerization for deployment)
- Logging & Testing Frameworks (Ensuring reliability and monitoring)


#  Future Enhancements
- Multi-turn conversation support
- Enhanced fact-checking for more reliable responses
- Real-time banking transaction analysis
- Web-based chatbot interface (FastAPI/Flask integration)


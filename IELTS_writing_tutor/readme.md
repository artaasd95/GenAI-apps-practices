# IELTS Writing Helping Agent API

## Overview

This project is a FastAPI-based service designed to assist users in improving their IELTS writing skills. It integrates a CSV-based knowledge base, a vector database, and a GPT model to provide personalized feedback, summaries, and insights on IELTS writing tasks.

## Features

- **Knowledge Base Integration**: Uses a CSV knowledge base containing sample IELTS writing essays, stored and managed with a PostgreSQL-backed vector database (`PgVector`).
- **Embedding Models**: Leverages OpenAI embeddings for vector representation of essay data.
- **Agent Functionality**: A custom agent, "IELTS Writing Helper," processes user queries, retrieves relevant examples, and provides tailored feedback or summaries.
- **API Endpoint**: Accepts user queries via a `/query` endpoint and returns helpful responses in JSON format.
- **Personalized Feedback**: Guides users on improving their writing skills based on existing examples and AI-generated suggestions.

## Technologies Used

- **FastAPI**: Framework for building the REST API.
- **PgVector**: PostgreSQL extension for efficient vector similarity searches.
- **Phi Framework**: Used for creating the custom agent and integrating knowledge bases and tools.
- **LangChain**: For managing the knowledge base and vectorized documents.
- **OpenAI GPT**: A GPT model (`gpt-4o-mini`) for natural language understanding and generation.
- **FAISS**: For efficient vector-based similarity searches.

## Directory Structure

```
.
├── app.py                   # Main API and agent logic
├── sample_data/             # Directory containing sample IELTS writing essays
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., OpenAI API key)
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ielts-writing-helper-api.git
   cd ielts-writing-helper-api
   ```

2. **Set up a Python virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the FastAPI server**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

2. **Query the Agent**:
   Use the `/query` endpoint to interact with the agent:
   - **Request Format**:
     ```json
     {
       "query": "Provide tips for improving my essay conclusion."
     }
     ```
   - **Response Format**:
     ```json
     {
       "response": "Your conclusion should restate your main points succinctly. Avoid introducing new ideas and ensure clarity."
     }
     ```

3. **Customize Data**:
   Add or update IELTS writing essays in the `sample_data/` directory. Ensure proper CSV formatting for seamless integration.

## Configuration

- **Knowledge Base Path**: Update the `sample_data/` directory in the code to point to your dataset.
- **PgVector Database**: Modify database configurations (e.g., table name, database URL) as needed.
- **Embedding Model**: Replace `OpenAIEmbeddings()` if using a different embedding model.

## Dependencies

- `faiss`
- `fastapi`
- `phi`
- `langchain_community`
- `langchain_openai`
- `uvicorn`
- `python-dotenv`

Install all dependencies with:
```bash
pip install -r requirements.txt
```


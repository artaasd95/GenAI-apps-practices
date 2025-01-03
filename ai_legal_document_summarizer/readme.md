# Law Document Expert API

## Overview

This project is a FastAPI-based service that uses a LangChain-powered knowledge base and a FAISS vector store for analyzing and summarizing legal documents. The `Agent` acts as an expert in law documents, capable of retrieving, summarizing, and providing insights based on user queries.

## Features

- **Document Loading**: Reads JSON files containing law documents using a directory loader.
- **Vector Search**: Leverages FAISS for fast and efficient similarity-based search.
- **Knowledge Base**: Uses LangChain's knowledge base powered by FAISS for context-aware document retrieval.
- **Agent**: A custom agent ("Law document expert") processes queries, searches the knowledge base, and returns concise summaries.
- **API Endpoint**: Accepts user queries via a `/query` endpoint and returns responses in JSON format.

## Technologies Used

- **FastAPI**: For building and serving the REST API.
- **FAISS**: For efficient vector-based similarity searches.
- **LangChain**: For creating a knowledge base from indexed documents.
- **OpenAI GPT**: A GPT model (`gpt-4o-mini`) for natural language understanding and generation.
- **Phi Framework**: For creating the custom agent and integrating tools.
- **LangChain Community Tools**: For document loading and vector store management.

## Directory Structure

```
.
├── ai_legal_document_summarizer_app.py     # Contains the API and agent logic
├── alaska-federal-reports/  # Directory containing JSON files with law documents
├── requirements.txt         # Python dependencies
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/law-document-expert-api.git
   cd law-document-expert-api
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

4. **Set OpenAI API credentials**:
   Ensure your OpenAI API key is set as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

## Usage

1. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. **Add data**:
   The data is just a sample you can download any legal document.
   This sample is downloaded from [Case Law](https://case.law/caselaw/)

## Configuration

- **Document Directory**: Update the path `../alaska-federal-reports` to point to your directory containing JSON law documents.
- **FAISS Embedding Model**: Modify or replace `OpenAIEmbeddings()` if a different embedding model is required.

## Dependencies

- `faiss`
- `fastapi`
- `phi`
- `langchain_community`
- `langchain_openai`
- `uvicorn`

Install all dependencies with:
```bash
pip install -r requirements.txt
```

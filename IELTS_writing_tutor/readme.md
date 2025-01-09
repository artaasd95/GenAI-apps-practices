# IELTS Writing Tutor API

## Overview

This project is a FastAPI-based service designed to help users prepare for IELTS writing tasks. The system combines a CSV knowledge base, a PostgreSQL-backed vector database, and OpenAI GPT to provide personalized guidance, example essays, and feedback on writing.

## Features

- **Knowledge Base Integration**: Uses a CSV knowledge base of sample IELTS writing essays, managed with a PostgreSQL-backed vector database (`PgVector`).
- **Embedding Models**: Employs OpenAI embeddings for efficient vector representation of essay data.
- **Agent Functionality**: A custom agent, "IELTS Writing Tutor," interacts with users, retrieves relevant essay examples, and provides tailored feedback and suggestions.
- **API Endpoint**: Accepts user queries via a `/query` endpoint and responds in JSON format.
- **Guided Writing Assistance**: Offers suggestions for writing styles, scores, and improvements, inspired by existing examples.

## Technologies Used

- **FastAPI**: Framework for creating the REST API.
- **PgVector**: PostgreSQL extension for vector similarity searches.
- **Phi Framework**: Facilitates the creation of the custom agent and integration of knowledge bases.
- **LangChain**: Manages knowledge base and embeddings.
- **OpenAI GPT**: Utilizes the `gpt-4o-mini` model for natural language processing.
- **Python Dotenv**: For managing environment variables.

## Directory Structure

```
.
├── app.py                   # Main API and agent implementation
├── sample_data/             # Directory containing sample IELTS writing essays
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., OpenAI API key)
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ielts-writing-tutor-api.git
   cd ielts-writing-tutor-api
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
   Interact with the agent using the `/query` endpoint:
   - **Request Format**:
     ```json
     {
       "query": "Provide examples of band 7 essays on environmental topics."
     }
     ```
   - **Response Format**:
     ```json
     {
       "response": "Here is an example of a band 7 essay on environmental protection: ..."
     }
     ```

3. **Customize Data**:
   Add or update IELTS writing examples in the `sample_data/` directory. Ensure the file is a properly formatted CSV.

## Configuration

- **Knowledge Base Path**: Update the path in `CSVKnowledgeBase` to point to your custom dataset.
- **Database Configuration**: Modify database connection details (e.g., table name, database URL) as required.
- **Model and Embeddings**: Adjust the `OpenAIChat` and `OpenAIEmbeddings` configurations if using alternative models or embeddings.

## Dependencies

- `faiss`
- `fastapi`
- `phi`
- `langchain_openai`
- `uvicorn`
- `python-dotenv`

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Additional Notes

- Ensure the PostgreSQL database with `PgVector` is set up and accessible.
- Use the agent's built-in instructions to customize user interactions further.
- This project is extensible for additional features, such as support for other writing tasks or exam formats.

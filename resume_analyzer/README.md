# HR Manager Agentic-AI

## Overview

The **HR Manager API** is a FastAPI-based application designed to analyze resumes, respond to HR-related queries, and provide insightful analyses of candidate qualifications. Leveraging advanced AI models and a PDF-based knowledge base, the API serves as a robust tool for Human Resources teams looking to streamline recruitment and resume review processes.

---

## Features

- **Natural Language Query Handling**: Processes user queries using OpenAI's advanced chat models.
- **Resume Knowledge Base**: Uses a PDF-based knowledge base to store, search, and analyze resumes.
- **Skills Matching**: Identifies individuals with specific skills or qualifications.
- **Session Management**: Maintains agent interaction history in a PostgreSQL database for consistency.
- **Dynamic Instructions**: Executes tasks based on detailed HR-centric instructions to ensure professional and actionable responses.
- **Chunked PDF Processing**: Efficiently processes large documents by dividing them into manageable chunks for analysis.

---

## API Endpoints

### `POST /ask`

Submit a query to the HR Manager API.

#### Request Body

- `query` (string, required): Your query or question related to resumes or HR tasks.

#### Response

- On success:
  ```json
  {
    "response": "Answer to the query"
  }
  ```
- On error:
  ```json
  {
    "error": "Error message"
  }
  ```

---

## Dependencies

- **OpenAIChat**: Powers the AI-driven query handling and response generation.
- **PDFKnowledgeBase**: Stores and retrieves information from uploaded PDF documents.
- **PgVector**: Facilitates vector-based search and retrieval within the knowledge base.
- **PgAgentStorage**: Handles session storage in PostgreSQL.
- **PDFReader**: Processes and parses resume PDFs into analyzable chunks.

---

## Key Components

- **Knowledge Base**: A PDF-based system for storing and retrieving resumes.
- **Agent**: The core intelligence system that answers queries and analyzes resumes based on predefined instructions.
- **PostgreSQL Integration**: Manages session data and historical interactions to enhance continuity in responses.
- **Dynamic Analysis**: Tailors responses to the query context by extracting relevant information from stored resumes.

---

## How It Works

1. **Query Handling**:  
   - Users submit queries through the `/ask` endpoint.
   - The agent processes the query using its knowledge base and instructions.

2. **Resume Analysis**:  
   - The knowledge base stores resumes in a vectorized format for efficient search and retrieval.
   - When a query is submitted, relevant resumes are analyzed for skills, experience, and qualifications.

3. **Session Management**:  
   - Maintains user sessions and interaction history to ensure continuity and accuracy in multi-step interactions.

---

## Notes

- Ensure the OpenAI API key is set in the environment (`OPENAI_API_KEY`).
- Configure the PostgreSQL database correctly for both agent session storage and resume knowledge base storage.
- Resumes should be uploaded as PDFs and will be processed in chunks to enable detailed analysis. 
- For running the knowledgebase like the example `Pgvector` you can run this command for docker:
  ```bash
    docker run -d -e POSTGRES_DB=ai -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -e PGDATA=/var/lib/postgresql/data/pgdata -v pgvolume:/var/lib/postgresql/data -p 5532:5432 --name pgvector phidata/pgvector:16
 ```

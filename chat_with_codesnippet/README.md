# GitHub Code Summarizer API

## Overview

This project is a FastAPI-based service that leverages advanced natural language models and GitHub integration to summarize and explain code repositories. The `Agent` acts as a professional code reviewer capable of retrieving, analyzing, and providing insights into GitHub repositories based on user queries.

## Features

- **GitHub Integration**: Interacts with GitHub repositories using access tokens for secure and efficient data retrieval.
- **Customizable Queries**: Accepts repository names and optional URLs for targeted analysis.
- **Postgres Storage**: Utilizes PostgreSQL for storing session histories and user interactions.
- **Code Analysis**: Reads, summarizes, and explains the purpose of code files in a repository.
- **Query Flexibility**: Can work with or without a specific repository URL.
- **API Endpoint**: Provides a `/summarize_repo` endpoint to handle user queries and return concise summaries.

## Technologies Used

- **FastAPI**: For building and serving the REST API.
- **Phi Framework**: For creating a customizable and extendable agent.
- **OpenAI GPT**: A GPT model (`gpt-4o-mini`) for natural language understanding and generation.
- **GitHub Tools**: For interacting with GitHub repositories and retrieving relevant information.
- **PostgreSQL**: For storing session histories and agent interactions.
- **dotenv**: For managing environment variables.

## Directory Structure

```
.
├── chat_with_code.py                     # Contains the API and agent logic
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (e.g., GitHub access token)
```

## Installation

1. **Clone the repository**:
   

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

4. **Set up environment variables**:
   Create a `.env` file in the project root and add the following:
   ```env
   GITHUB_ACCESS_TOKEN="your_github_access_token"
   ```

5. **Set up PostgreSQL**:
   Ensure a PostgreSQL database is running and accessible. Update the `db_url` in the `PgAgentStorage` configuration with your database credentials.
   you can use this command to run Pgvector in Docker from the documentation of Phidata:
   ```bash
      docker run -d \
     -e POSTGRES_DB=ai \
     -e POSTGRES_USER=ai \
     -e POSTGRES_PASSWORD=ai \
     -e PGDATA=/var/lib/postgresql/data/pgdata \
     -v pgvolume:/var/lib/postgresql/data \
     -p 5532:5432 \
     --name pgvector \
     phidata/pgvector:16
   ```


## Usage

1. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   Example response:
   ```json
   {
       "response": "The repository 'phidatahq/phidata' contains tools for data workflows..."
   }
   ```

## Configuration

- **GitHub Access Token**: Ensure a valid GitHub personal access token is set in the `.env` file for repository interactions.
- **Postgres Configuration**: Update the `db_url` in the `PgAgentStorage` initialization to connect to your database.
- **Agent Session Settings**:
  - Modify `session_id` and `user_id` logic as required.
  - Adjust `num_history_responses` for the number of history records stored.

## Dependencies

- `fastapi`
- `phi`
- `langchain_openai`
- `uvicorn`
- `psycopg`
- `python-dotenv`

Install all dependencies with:
```bash
pip install -r requirements.txt
```


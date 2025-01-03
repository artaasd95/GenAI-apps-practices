# Unified Agent API

## Overview

The **Unified Agent API** is a FastAPI-based application designed to serve as an intelligent agent that can answer questions, analyze repositories, provide financial insights, and interact with knowledge bases. The application integrates various tools and libraries to create a powerful and flexible system for answering queries and handling complex tasks.

---

## Features

- **Natural Language Query Handling**: Processes and answers queries using advanced language models (e.g., OpenAIChat).
- **Knowledge Base Integration**: Uses a FAISS-backed knowledge base to retrieve and analyze relevant information efficiently.
- **Tool Integration**:
  - **YFinanceTools**: Fetch stock prices, analyst recommendations, and financial fundamentals.
  - **CsvTools**: Analyze and summarize CSV files.
- **Repository Summarization**: Supports searching and analyzing GitHub repositories to answer code-related questions.
- **Session Management**: Uses PostgreSQL storage to maintain agent sessions and interaction history.
- **Dynamic Instructions**: Executes tasks based on detailed, multi-step instructions to ensure accurate responses.

---

## API Endpoints

### `POST /ask`

Submit a query to the Unified Agent.

#### Request Body
- `query`: (string) Your query or question.
- `repository_url` (optional): (string) URL of a GitHub repository for context-specific questions.

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

Due to the variations in versions of **LangChain** and **PhiData**, it is highly recommended to check the installed and used libraires and install the appropriate versions of the required libraries to ensure compatibility.
Important: You might need to change some of the requirements

---

## Key Components

- **FAISS Vector Store**: Utilized for efficient similarity search and retrieval.
- **LangChainKnowledgeBase**: Powers the knowledge base retrieval system.
- **Agent Storage**: Stores session data and interaction history in a PostgreSQL database.

---

## How It Works

1. **Query Handling**: 
   - Accepts user queries through the `/ask` endpoint.
   - If a repository URL is provided, the agent fetches and summarizes the repository before answering.
   
2. **Tool Usage**:
   - The agent employs tools like YFinanceTools and CsvTools for domain-specific tasks.
   - Integrates historical knowledge using the FAISS-based knowledge base.

3. **Dynamic Responses**:
   - Generates responses based on instructions and the tools used during the session.

---

## Notes

For smooth operation:
- Ensure the OpenAI API key is set in the environment (`OPENAI_API_KEY`).
- PostgreSQL database configuration is correctly set up for session storage.
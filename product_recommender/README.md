# Product Recommender API

## Overview

This project is a FastAPI-based service designed to assist users in finding and learning about products. It integrates a LangChain knowledge base with a Milvus vector store and OpenAI GPT model to deliver personalized product recommendations and summaries.

## Features

- **CSV-Based Knowledge Base**: Dynamically loads product data from CSV files in the specified directory.
- **Vector Store Integration**: Uses Milvus for efficient storage and retrieval of vectorized product data.
- **Embedding Models**: Utilizes OpenAI embeddings for generating vector representations of product information.
- **Agent Functionality**: A custom agent, "Product Recommender," interacts with users, retrieves relevant products, and summarizes their descriptions.
- **API Endpoint**: Accepts user queries via a `/query` endpoint and provides detailed responses in JSON format.
- **Personalized Recommendations**: Offers tailored product suggestions based on user queries and retrieved knowledge.

## Technologies Used

- **FastAPI**: Framework for building the REST API.
- **Milvus**: Vector database for similarity searches.
- **Phi Framework**: Used for creating the custom agent and integrating knowledge bases.
- **LangChain**: Facilitates document loading and vectorized queries.
- **OpenAI GPT**: Leverages the `gpt-4o-mini` model for natural language processing.
- **Python Dotenv**: Manages environment variables.

## Directory Structure

```
.
├── app.py                   # Main API and agent logic
├── your_directory_path/     # Directory containing CSV files with product data
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., OpenAI API key)
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/product-recommender-api.git
   cd product-recommender-api
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

1. **Prepare CSV Data**:
   - Add product data as CSV files to the `your_directory_path/` directory.
   - Ensure each file follows a consistent format, with headers like `Index`, `Height`, `Weight`, etc. Update the field names in the code to match your data structure.

2. **Run the FastAPI server**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

3. **Query the Agent**:
   Use the `/query` endpoint to interact with the product recommender:
   - **Request Format**:
     ```json
     {
       "query": "Recommend a lightweight laptop for office use."
     }
     ```
   - **Response Format**:
     ```json
     {
       "response": "Here are some recommended lightweight laptops for office use: ..."
     }
     ```

4. **Customize Data**:
   - Modify the `your_directory_path` directory and update the CSV loading logic in the code to fit your specific dataset.
   - Adjust the knowledge base configurations or embedding model as needed.

## Configuration

- **Knowledge Base Path**: Update the `directory_path` variable to point to your dataset.
- **Milvus Vector Store**: Modify the `URI` for the database connection as required.
- **CSV File Format**: Ensure the field names in the `csv_args` match your dataset schema.
- **Model and Embeddings**: Replace `OpenAIChat` and `OpenAIEmbeddings` with alternative models or embeddings if needed.

## Dependencies

- `faiss`
- `fastapi`
- `phi`
- `langchain_community`
- `langchain_openai`
- `langchain_milvus`
- `uvicorn`
- `python-dotenv`

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Additional Notes

- Ensure that the Milvus vector store is properly set up and accessible.
- Customize the agent's instructions for specific interaction styles or use cases.
- Extend the system to support additional product categories or data sources.

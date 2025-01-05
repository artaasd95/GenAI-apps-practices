import os
import faiss
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from phi.knowledge.langchain import LangChainKnowledgeBase
from phi.agent import Agent
from phi.tools.csv_tools import CsvTools
from phi.knowledge.csv import CSVKnowledgeBase
from phi.vectordb.pgvector import PgVector, SearchType
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()



embedding = OpenAIEmbeddings()

ielts_writing = 'sample_data/ielts-writing-essays.csv'

knowledge_base = CSVKnowledgeBase(
    path="sample_data",
    # Table name: ai.csv_documents
    vector_db=PgVector(
        table_name="ielts_writings",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)


agent = Agent(
    name="Law document expert",
    description="You are the expert analyzer of the law documents",
    model=OpenAIChat(id='gpt-4o-mini'),
    knowledge_base=knowledge_base,
    search_knowledge=True,
    instructions=[
        "Greet only at the first time",
        "Get list of files",
        "Analyze the files",
        "Search knowledgebase for the documents and retrieve the most similar.",
        "summarize documents and return the summary of them",
    ]
)

agent.knowledge.load(recreate=False)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_agent(request: QueryRequest):
    user_query = request.query
    if not user_query:
        return JSONResponse({"error": "No query provided"}, status_code=400)
    answer = agent.run(user_query)
    answer = answer.to_dict().get('content')
    return JSONResponse({"response": answer})

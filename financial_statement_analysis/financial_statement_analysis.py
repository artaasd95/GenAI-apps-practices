from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import faiss
from langchain_community.vectorstores import FAISS as CommunityFAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.knowledge.langchain import LangChainKnowledgeBase
from phi.tools.yfinance import YFinanceTools
from phi.tools.csv_tools import CsvTools
from phi.storage.agent.postgres import PgAgentStorage
from dotenv import load_dotenv
import httpx
from pathlib import Path
import os
import uuid

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()


agent_storage = PgAgentStorage(
    table_name="agent_sessions",
    db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
)

index = faiss.IndexFlatL2(len(OpenAIEmbeddings().embed_query("hello world")))
faiss_vector_store = CommunityFAISS(
    embedding_function=OpenAIEmbeddings(),
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)
knowledge_base = LangChainKnowledgeBase(retriever=faiss_vector_store.as_retriever())


agent = Agent(
    name="Unified Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),
        CsvTools(csvs=[])
    ],
    knowledge_base=knowledge_base,
    instructions=[
        "First get the repo if available and search the whole repository using the tool",
        "If no repository url is passed, search for the similar codes in the github using the tool",
        "Read the whole repository if any chosen from the previous messages or any repo pointed out",
        "Answer the questions based on the code you have read and you have access to",
        "yoo should get the question",
        "if the user wanted financial statement, use yfinance tool to read it",
        "use knowledgebase for read preious data, if needed get the new data from the yfinance tool",
        "if any files added to csv tool read all of them",
        "summarize the tables in csv files read them and get ready to answer based on them"
    ],
    session_id=str(uuid.uuid4()),
    user_id=str(uuid.uuid4()),
    add_history_to_messages=True,
    show_tool_calls=True,
    num_history_responses=10,
    storage=agent_storage
)

class QueryRequest(BaseModel):
    query: str = Field(..., description="Your query or question")
    

@app.post("/ask")
async def ask_question(query_request: QueryRequest):
    if query_request.repository_url:
        final_query = f"Summarize the repository at {query_request.repository_url} and answer: {query_request.query}"
    else:
        final_query = query_request.query
    try:
        response = agent.run(final_query)
        return JSONResponse({"response": response.to_dict().get('content')})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

import os
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from phi.agent import Agent
from phi.knowledge.csv import CSVKnowledgeBase
from phi.vectordb.pgvector import PgVector
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
    vector_db=PgVector(
        table_name="ielts_writings",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)


agent = Agent(
    name="IELTS Writing tutor",
    description="You are a tutor for IELTS writing task",
    model=OpenAIChat(id='gpt-4o-mini'),
    knowledge_base=knowledge_base,
    search_knowledge=True,
    instructions=[
        "Greet only at the first time",
        "Get list of files",
        "Analyze the files",
        "If the user wanted to write a text for an IELTS writing exam, write a proper text",
        "you can find some similar writing answers to inspire by them",
        "if the user wanted different styles and scores for writing search knowledge base and show the answers",
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

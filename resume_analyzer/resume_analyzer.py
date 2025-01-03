from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector
from phi.storage.agent.postgres import PgAgentStorage
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()

agent_storage = PgAgentStorage(
    table_name="agent_sessions",
    db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
)
pdf_knowledge_base = PDFKnowledgeBase(
    path="resumes",
    vector_db=PgVector(
        table_name="resumes",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
    reader=PDFReader(chunk=True),
)
agent = Agent(
    name="HR Manager",
    description="HR manager who can read resumes and analyze them",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[],
    knowledge_base=pdf_knowledge_base,
    instructions=[
        "Gather user queries about resumes and HR documents",
        "Analyze relevant PDF documents from the knowledge base",
        "Find individuals with specific skills",
        "Respond with a concise analysis focused on experience, skills, and qualifications",
        "Use professional and clear language suitable for HR interactions",
        "Separate each individual with names and personal details from their data",
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
    final_query = query_request.query
    try:
        response = agent.run(final_query)
        return JSONResponse({"response": response.to_dict().get('content')})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

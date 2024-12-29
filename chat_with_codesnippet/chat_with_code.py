from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from phi.agent import Agent
from phi.tools.github import GithubTools
from langchain_openai import OpenAIChat
from phi.storage.agent.postgres import PgAgentStorage
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")

agent_storage = PgAgentStorage(
                table_name="agent_sessions",
                db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
                )

app = FastAPI()

# Pydantic model for query requests
class QueryRequest(BaseModel):
    query: str = Field(..., description="The query or action to perform on the repository.")
    repository_url: str = Field(None, description="Optional URL of the repository.")

# Define the agent with tools to interact with GitHub and summarize code
agent = Agent(
    name="GitHub Code Summarizer",
    description="You are a pro code reviewer, you can read, analyze and understand codes",
    model=OpenAIChat(id='gpt-4o-mini'),
    tools=[GithubTools(access_token=github_access_token)],
    instructions=[
        "First get the repo if available and search the whole repository using the tool",
        "If no repository url is passed, search for the similar codes in the github using the tool",
        "Read the whole repository if any chosen from the previous messages or any repo pointed out",
        "Answer the questions based on the code you have read and you have access to",
    ],
    show_tool_calls=True,
    session_id=str(uuid.uuid4),
    user_id=str(uuid.uuid4), #Sample ids
    add_history_to_messages=True,
    num_history_responses=10,
    storage=agent_storage,


)

@app.post("/summarize_repo")
async def summarize_repository(query_request: QueryRequest):
    repo_name = query_request.query
    repository_url = query_request.repository_url

    if not repo_name:
        return JSONResponse({"error": "No repository name provided"}, status_code=400)

    try:
        # Use the agent to analyze the repository
        if repository_url:
            response = agent.run(f"Summarize the repository {repo_name} located at {repository_url} and explain its code.")
        else:
            response = agent.run(f"Summarize the repository {repo_name} and explain its code.")
        return JSONResponse({"response": response})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

import os
import faiss
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from phi.knowledge.langchain import LangChainKnowledgeBase
from phi.agent import Agent

from langchain_community.document_loaders import DirectoryLoader, JSONLoader
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()

loader = DirectoryLoader(
    "../alaska-federal-reports",
    glob="**/*.json",
    loader_cls=JSONLoader
)
documents = loader.load()

embedding = OpenAIEmbeddings()
index = faiss.IndexFlatL2(len(embedding.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embedding,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

vector_store.add_documents(documents)
retriever = vector_store.as_retriever()

knowledge_base = LangChainKnowledgeBase(retriever=retriever)

agent = Agent(
    name="Law document expert",
    description="You are the expert analyzer of the law documents",
    model=OpenAIChat(id='gpt-4o-mini'),
    knowledge_base=knowledge_base,
    instructions=[
        "Greet only at the first time",
        "You have to get the user query about law documents.",
        "Search knowledgebase for the documents and retrieve the most similar.",
        "summarize documents and return the summary of them",
    ]
)

@app.post("/query")
async def query_agent(request: Request):
    data = await request.json()
    user_query = data.get("query", "")
    if not user_query:
        return JSONResponse({"error": "No query provided"}, status_code=400)
    answer = agent.run(user_query)
    return JSONResponse({"response": answer})

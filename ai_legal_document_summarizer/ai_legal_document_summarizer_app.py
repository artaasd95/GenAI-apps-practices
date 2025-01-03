import os
import faiss
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from phi.knowledge.langchain import LangChainKnowledgeBase
from phi.agent import Agent
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()



embedding = OpenAIEmbeddings()
index = faiss.IndexFlatL2(len(embedding.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embedding,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

directory_path = "law_corpuses/alaska-federal-reports"
file_list = [
    os.path.join(root, file)
    for root, _, files in os.walk(directory_path)
    for file in files if file.endswith(".json")
]
documents = []

for file_path in file_list:
    loader = JSONLoader(jq_schema='.', file_path=file_path,
                        text_content=False)
    file_documents = loader.load()
    documents.extend(file_documents)


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

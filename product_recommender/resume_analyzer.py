import os
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from phi.knowledge.langchain import LangChainKnowledgeBase
from phi.agent import Agent
from langchain_community.document_loaders import CSVLoader
from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings
from langchain_core import LangChainKnowledgeBase
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()

directory_path = './your_directory_path'
docs = []
embedding = OpenAIEmbeddings()
URI = "./milvus_example.db"

# Initialize the Milvus vector store with OpenAI embeddings
vector_store = Milvus(
    embedding_function=OpenAIEmbeddings(),
    connection_args={"uri": URI},
)

for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(directory_path, filename)
        loader = CSVLoader(
            file_path=file_path,
            csv_args={
                'delimiter': ',',
                'quotechar': '"',
                'fieldnames': ['Index', 'Height', 'Weight']#Change base on the data
            }
        )
        loaded_docs = loader.load()
        docs.extend(loaded_docs)  # Add loaded documents to the list
vector_store.add_documents(docs)
# Get a retriever from the vector store, which allows querying the knowledge base
retriever = vector_store.as_retriever()

# Create a LangChain knowledge base from the retriever
knowledge_base = LangChainKnowledgeBase(retriever=retriever)



agent = Agent(
    name="product recommender",
    description="You are a seller and product expert",
    model=OpenAIChat(id='gpt-4o-mini'),
    knowledge_base=knowledge_base,
    instructions=[
        "Greet only at the first time",
        "You have to get the user inquery about any produt",
        "Search knowledgebase for the products and retrieve the most similar.",
        "summarize product description and return the summary of them",
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

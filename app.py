from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY  # type: ignore
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY  # type: ignore


embeddings = download_embeddings()

index_name = "medical-rag-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name, embedding=embeddings
)


retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 8},
)


chatModel = ChatGroq(model="openai/gpt-oss-20b")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


# ** Routes:


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name="chat.html", request=request, context={"request": request}
    )  # type: ignore


@app.post("/get")
async def chat(msg: str = Form(...)):
    response = rag_chain.invoke({"input": msg})
    # print(response['answer'])
    return {"answer": response["answer"]}




















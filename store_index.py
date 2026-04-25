from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
import os
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from src.helper import download_embeddings, filter_to_minimal_docs, load_pdf_files, text_split

load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY  # type: ignore
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY  # type: ignore



extracted_data = load_pdf_files("./data")
minimal_docs = filter_to_minimal_docs(extracted_data)
texts_chunks = text_split(minimal_docs)


embeddings=download_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)


index_name = "medical-rag-chatbot"


if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )


index = pc.Index(index_name)


vector_store = PineconeVectorStore.from_documents(
    documents=texts_chunks, embedding=embeddings, index_name=index_name
)







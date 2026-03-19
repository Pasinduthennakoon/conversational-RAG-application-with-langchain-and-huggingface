from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from .embedding import embedding_model

#PDF Loader
loader = PyPDFLoader("data/codeprolk.pdf")
docs = loader.load()

#Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)
splits = text_splitter.split_documents(docs)

vector_store = FAISS.from_documents(
    documents=splits,
    embedding=embedding_model
)

retriever = vector_store.as_retriever()
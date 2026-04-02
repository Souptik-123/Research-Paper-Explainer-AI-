from langchain.vectorstores import FAISS
from config import TOP_K

def create_vectorstore(docs, embeddings):
    return FAISS.from_texts(docs, embeddings)

def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": TOP_K})
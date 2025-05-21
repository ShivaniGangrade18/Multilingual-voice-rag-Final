from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ updated
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def build_vectorstore():
    loader = TextLoader("data.txt")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # ✅ updated
    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore

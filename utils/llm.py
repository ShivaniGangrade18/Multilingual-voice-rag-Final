from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def get_qa_chain(vectorstore):
    llm = ChatGroq(
        temperature=0,
        model_name="llama3-8b-8192",  # ✅ updated to supported model
        api_key=os.getenv("GROQ_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain

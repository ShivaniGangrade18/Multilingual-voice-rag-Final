from utils.speech import speech_to_text, text_to_speech
from utils.retriever import build_vectorstore
from utils.llm import get_qa_chain

def main():
    print("✅ Program started.")

    query = speech_to_text()

    if not query:
        print("⚠️ No speech was detected. Exiting...")
        return

    print("🔍 Building vector store...")
    vectorstore = build_vectorstore()

    print("🤖 Connecting to QA chain...")
    qa = get_qa_chain(vectorstore)

    print("🧠 Asking AI...")
    response = qa.run(query)

    print("🤖 Response:", response)

    text_to_speech(response)

if __name__ == "__main__":
    print("🟢 Calling main()...")
    main()
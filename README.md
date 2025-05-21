# 🎙️ AI-Powered Voice Assistant with RAG

This project is a voice-interactive assistant built using Python. It listens to the user's spoken questions, retrieves relevant context using RAG (Retrieval-Augmented Generation), and provides answers using a language model. The assistant responds by speaking the answer aloud, making it highly user-friendly and accessible.

---

## 🛠 Technologies Used

| Component             | Tool/Library                            |
|-----------------------|-----------------------------------------|
| Voice Input           | `speech_recognition`                    |
| Text-to-Speech Output | `gTTS`                                  |
| Language Model        | OpenAI's GPT-3.5 via LangChain          |
| Vector Search         | FAISS (with HuggingFace Embeddings)     |
| IDE                   | Visual Studio Code                      |
| Python Version        | 3.10.11                                 |

---

## 🚀 How to Run the Project

### 1. Clone or Download the Repository
```bash
git clone <repository-url>
# Create and Activate a Virtual Environment:-
python -m venv venv
.\venv\Scripts\activate
# Install Dependencies:-
pip install -r requirements.txt
#Configure the OpenAI API Key
#Prepare Your Knowledge Base:-
Create a text file named data.txt in the root folder.
Add content that the assistant should reference for answers
# Run the Assistant:-
Open your terminal and run:
python main.py
⚠️ Important: Run the script only from the terminal to ensure it uses the correct virtual environment. Avoid using the VS Code run button (▶️).
###🧾 Project Overview
multilingual_voice_rag/
│
├── main.py                 # Main application logic
├── .env                    # Environment variables (API key)
├── data.txt                # Text used for retrieval
├── requirements.txt        # Python dependencies
├── utils/
│   ├── speech.py           # Voice input/output functions
│   ├── retriever.py        # Vector search setup using FAISS
│   └── llm.py              # OpenAI model integration
└── venv/                   # Virtual environment folder
####✅ Working Process (Plagiarism-Free)
The voice assistant operates by listening to the user's spoken input through a microphone. It first converts the audio to text using a speech recognition library. Once the question is transcribed, the system uses a retrieval-based approach to search for relevant information within a predefined knowledge base (data.txt). This is done using FAISS for vector-based similarity search, combined with HuggingFace embeddings to convert text into semantic vectors. The most relevant chunks of text are then passed to a large language model (OpenAI’s GPT-3.5) using LangChain, which generates a natural language answer. Finally, the response is converted back into speech using a text-to-speech engine (gTTS) and played aloud to the user. The entire process is handled in real-time, creating an intelligent voice-driven Q&A experience.
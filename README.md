# 🧠 Football RAG Assistant (Conversational AI System)

An end-to-end **Retrieval-Augmented Generation (RAG)** based conversational AI system for answering football-related queries using custom knowledge (PDF documents).

This project integrates:

* **LangChain** for orchestration
* **NVIDIA Nemotron LLM** for responses
* **HuggingFace** embedding model
* **FAISS** for vector search
* **FastAPI** backend
* **Streamlit** frontend
* **Docker Compose** for full system deployment

---

## 🚀 Features

* 📄 PDF-based knowledge ingestion (Football dataset)
* 🔍 Semantic search using embeddings
* 💬 Conversational memory (session-based chat)
* 🧠 History-aware question reformulation
* ⚡ FastAPI REST API backend
* 🎨 Streamlit interactive UI
* 🐳 Fully containerized with Docker

---

## 🏗️ System Architecture

```
User (Streamlit UI)
        ↓
FastAPI Backend (/chat endpoint)
        ↓
Conversational RAG Chain
   ├── History-aware Retriever
   ├── FAISS Vector Store
   ├── Embedding Model (HuggingFace)
   └── LLM (NVIDIA Nemotron)
```

---

## 📂 Project Structure

```
project-root/
│
├── backend/
│   ├── utils/
│   │   ├── model.py
│   │   ├── embedding.py
│   │   ├── retriever.py
│   │   ├── chain.py
│   │   ├── output.py
│   │   ├── prompts.py
│   │   ├── history_aware_retriever.py
│   │   └── chat_session_history.py
│   ├── data/
│   │   └── football.pdf
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
NVIDIA_API_KEY=your_nvidia_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

## 🐳 Docker Setup (Recommended)

### 1. Build & Run

```bash
docker-compose up --build
```

### 2. Access Applications

* Backend API:
  👉 http://localhost:8000/docs

* Frontend UI:
  👉 http://localhost:8501

---

## 💻 Local Development Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🔗 API Endpoint

### POST `/chat`

#### Request

```json
{
  "input": "What is football?",
  "session_id": "101"
}
```

#### Response

```json
{
  "answer": "Football is a sport...",
  "session_id": "101"
}
```

---

## 🧠 Core Components

### 1. Embeddings

* Model: `sentence-transformers/all-mpnet-base-v2`
* Converts text → vectors for semantic search

### 2. Vector Store

* FAISS for efficient similarity search

### 3. Retriever

* Retrieves relevant document chunks

### 4. History-Aware Retriever

* Reformulates user queries using chat history

### 5. LLM

* NVIDIA Nemotron (120B) for response generation

---

## 💬 Conversational Memory

* Maintains chat sessions using `session_id`
* Enables context-aware conversations

---

## 📊 Example Workflow

1. User asks a question
2. System reformulates it (if needed)
3. Retrieves relevant document chunks
4. Passes context + query to LLM
5. Returns grounded response

---

## ⚠️ Notes

* Ensure internet access for:

  * NVIDIA API
  * HuggingFace embeddings
* If running in Docker, **do NOT use `localhost` inside containers**

  * Use service name: `http://backend:8000`

---

## 🛠️ Troubleshooting

### ❌ Connection Errors

* Ensure backend container is healthy:

```bash
docker ps
```

### ❌ API not reachable

* Check logs:

```bash
docker-compose logs backend
```

### ❌ DNS / Network Issues

* Verify internet connectivity inside container

---

## 📌 Future Improvements

* Add multi-document upload support
* Implement hybrid search (BM25 + vector)
* Add user authentication
* Deploy to cloud (AWS / GCP / Azure)
* Add evaluation metrics for RAG quality

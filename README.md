# 🚀 PDF RAG Assistant (Local AI)

An end-to-end Retrieval-Augmented Generation (RAG) system that allows users to upload PDFs and ask questions using a local LLM (Ollama).

---

## 🔥 Features

* Multi-PDF Upload
* Semantic Search (FAISS)
* Local LLM (No API cost)
* FastAPI Backend
* Persistent Vector Store

---

## 🛠️ Tech Stack

* Python
* FastAPI
* FAISS
* Sentence Transformers
* Ollama (LLaMA / Mistral)

---

## ⚡ Setup (Run Locally)

```bash
git clone https://github.com/Bhaskar86gh/pdf-rag-assistant.git
cd pdf-rag-assistant
pip install -r requirements.txt
```

---

## ▶️ Start Server

```bash
fastapi dev main.py
```

Open:
👉 http://127.0.0.1:8000/docs

---

## 🧪 How to Use

1. Upload PDF files
2. Ask questions like:

   * "What are the project requirements?"
   * "Summarize the document"
3. Get AI-generated answers

---

## 🧠 Model Setup (IMPORTANT)

Make sure Ollama is running:

```bash
ollama run mistral
```

---

## 📌 Future Improvements

* UI dashboard
* Chat history
* Deployment (Render / Docker)
* Streaming responses

---

## 👨‍💻 Author

Bhaskar

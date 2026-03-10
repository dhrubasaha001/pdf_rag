# PDF RAG System

A simple **Retrieval-Augmented Generation (RAG)** system that allows users to upload a PDF and ask questions about its content.

The system extracts text from the PDF, creates embeddings, stores them in a FAISS vector index, and uses an LLM to generate answers based on the retrieved context.

---

## Architecture

User → Streamlit Frontend → FastAPI Backend → Retriever (FAISS) → LLM → Response

Components:

* **Streamlit** – User interface
* **FastAPI** – Backend API
* **FAISS** – Vector similarity search
* **Sentence Transformers** – Text embeddings
* **Ollama + Mistral** – Language model for answer generation

---

## Project Structure

```
RAG_PDF_Project/
│
├── backend/
│   ├── main.py
│   ├── schemas.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── frontend/
│   └── app.py
│
├── data/
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository and install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Backend

```
uvicorn backend.main:app --reload
```

---

## Run the Frontend

```
streamlit run frontend/app.py
```

---

## Usage

1. Upload a PDF document.
2. Ask questions about the document.
3. The system retrieves relevant chunks from the document using FAISS.
4. The LLM generates an answer based on the retrieved context.

---

## Features

* PDF document ingestion
* Vector similarity search with FAISS
* Retrieval-Augmented Generation pipeline
* FastAPI backend
* Streamlit frontend

---

## Future Improvements

* Better document chunking
* Persistent vector storage
* Multi-document support
* Improved UI
* Streaming LLM responses


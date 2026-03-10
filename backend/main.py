from fastapi import FastAPI, UploadFile, File
from schemas import Question
from rag_pipeline import ask_question
from retriever import process_document
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to PDF RAG"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("data", exist_ok=True)

    contents = await file.read()
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(contents)

    process_document(file_path)

    return {"message": "PDF uploaded and indexed"}


@app.post("/ask")
def ask(data: Question):

    answer = ask_question(data.question)

    return {"answer": answer}
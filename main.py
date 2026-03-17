from fastapi import FastAPI, UploadFile, File
from typing import List
import json
import os

app = FastAPI()

from rag.vector_store import build_index, search, load_index

# Load existing data
index, all_chunks = load_index()

FILES_PATH = "data/files.json"

if os.path.exists(FILES_PATH):
    with open(FILES_PATH, "r") as f:
        uploaded_files = json.load(f)
else:
    uploaded_files = []


@app.post("/upload_pdf")
async def upload_pdf(files: List[UploadFile] = File(...)):

    global uploaded_files
    global all_chunks
    global index

    from rag.pdf_loader import load_pdf
    from rag.chunker import chunk_text
    from rag.embeddings import embed_texts

    new_chunks = []

    for file in files:

        content = await file.read()

        text = load_pdf(content)

        chunks = chunk_text(text)

        new_chunks.extend(chunks)

        uploaded_files.append(file.filename)

    if not new_chunks:
        return {"error": "No content extracted"}

    all_chunks.extend(new_chunks)

    embeddings = embed_texts(all_chunks)

    index = build_index(embeddings, all_chunks)

    # Save file names
    os.makedirs("data", exist_ok=True)
    with open(FILES_PATH, "w") as f:
        json.dump(uploaded_files, f)

    return {
        "message": "Files uploaded successfully",
        "files": uploaded_files,
        "total_chunks": len(all_chunks)
    }


@app.get("/ask")
def ask(q: str):

    from rag.embeddings import embed_query
    from llm.ollama_client import generate

    global index
    global all_chunks

    if index is None:
        return {"error": "No documents uploaded yet"}

    query_embedding = embed_query(q)

    context_chunks = search(index, all_chunks, query_embedding, k=3)

    context = "\n".join(context_chunks)

    answer = generate(q, context)

    return {"answer": answer}


@app.get("/documents")
def documents():

    global uploaded_files
    global all_chunks

    return {
        "total_files": len(uploaded_files),
        "files": uploaded_files,
        "total_chunks": len(all_chunks)
    }
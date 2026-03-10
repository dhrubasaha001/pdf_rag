from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Global variables
index = None
chunks = None


def process_document(file_path):

    global index, chunks

    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # simple chunking
    chunks = text.split("\n")

    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)


def search_chunks(query, k=3):

    global index, chunks

    query_vector = model.encode([query])

    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = [chunks[i] for i in indices[0]]

    return results
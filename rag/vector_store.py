import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "data/index.faiss"
DOC_PATH = "data/docs.pkl"


def save_index(index, documents):

    if not os.path.exists("data"):
        os.makedirs("data")

    faiss.write_index(index, INDEX_PATH)

    with open(DOC_PATH, "wb") as f:
        pickle.dump(documents, f)


def load_index():

    if os.path.exists(INDEX_PATH) and os.path.exists(DOC_PATH):

        index = faiss.read_index(INDEX_PATH)

        with open(DOC_PATH, "rb") as f:
            documents = pickle.load(f)

        return index, documents

    return None, []


def build_index(embeddings, texts):

    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))

    save_index(index, texts)

    return index


def search(index, documents, query_embedding, k=3):

    D, I = index.search(
        np.array(query_embedding).astype("float32"), k
    )

    return [documents[i] for i in I[0]]
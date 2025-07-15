from sentence_transformers import SentenceTransformer
import numpy as np, json, os

model = SentenceTransformer("all-MiniLM-L6-v2")
memory_vectors = []

def log_memory(text, source):
    vec = model.encode(text)
    memory_vectors.append({"vector": vec.tolist(), "source": source})

def similarity_search(query):
    qvec = model.encode(query)
    return sorted(memory_vectors, key=lambda x: np.dot(qvec, x["vector"]), reverse=True)
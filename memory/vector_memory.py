import faiss
import numpy as np

class NeuralMemory:
    def __init__(self, dim=128):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []

    def encode(self, signal_record: dict) -> np.ndarray:
        vec = np.random.rand(self.index.d)  # Placeholder: replace with real encoder
        return vec

    def insert(self, signal_record: dict):
        vec = self.encode(signal_record)
        self.index.add(np.array([vec]).astype('float32'))
        self.data.append(signal_record)

    def search(self, query_record: dict, top_k=5):
        query_vec = self.encode(query_record)
        D, I = self.index.search(np.array([query_vec]).astype('float32'), top_k)
        return [self.data[i] for i in I[0]]
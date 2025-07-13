from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class MemoryEncoder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def encode_signal_history(self, signal_list):
        texts = [f"{s['strategy']} {s['signal']} {s['symbol']} {s['price']}" for s in signal_list]
        matrix = self.vectorizer.fit_transform(texts)
        return matrix.toarray()

    def similarity_matrix(self, embeddings):
        norm = np.linalg.norm(embeddings, axis=1, keepdims=True)
        normalized = embeddings / (norm + 1e-8)
        return np.dot(normalized, normalized.T)
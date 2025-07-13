import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from memory.memory_encoder import MemoryEncoder

# Fake signal data (real: load from logs)
signals = [
    {"strategy": "Trend", "signal": "buy", "symbol": "AAPL", "price": 123},
    {"strategy": "MeanReversion", "signal": "sell", "symbol": "AAPL", "price": 128},
    {"strategy": "Trend", "signal": "sell", "symbol": "BTC", "price": 19500},
    {"strategy": "Breakout", "signal": "buy", "symbol": "ETH", "price": 3450},
    # ...
]

encoder = MemoryEncoder()
X = encoder.encode_signal_history(signals)

pca = PCA(n_components=2)
coords = pca.fit_transform(X)

st.title("📍 Signal Memory Embedding Cluster")

fig, ax = plt.subplots()
ax.scatter(coords[:, 0], coords[:, 1], alpha=0.8)
for i, s in enumerate(signals):
    ax.annotate(s["strategy"], (coords[i, 0], coords[i, 1]))
st.pyplot(fig)
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import json

st.title("🧬 Venture Lineage Explorer")

G = nx.DiGraph()
with open("logs/forks.jsonl") as f:
    for line in f:
        fork = json.loads(line)
        G.add_edge(fork.get("parent", "root"), fork["sim"])

fig, ax = plt.subplots(figsize=(12, 6))
nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray", ax=ax)
st.pyplot(fig)
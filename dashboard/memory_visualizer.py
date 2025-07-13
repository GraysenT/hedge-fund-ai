import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from memory.strategy_lineage_graph import StrategyLineageGraph

st.set_page_config(layout="wide")
st.title("🧠 Strategy Lineage Visualizer")

lineage = StrategyLineageGraph()
# Load from stored graph (optional)
# lineage.load("path.json")

G = lineage.graph
fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.3)
nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)
st.pyplot(fig)
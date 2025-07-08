import json
import networkx as nx
import matplotlib.pyplot as plt

with open("strategy_memory/strategy_lineage.json") as f:
    lineage = json.load(f)

G = nx.DiGraph()

for strat, info in lineage.items():
    parent = info.get("parent", "ROOT")
    G.add_edge(parent, strat)

plt.figure(figsize=(16, 10))
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=8)
plt.title("📚 Strategy Lineage Tree")
plt.show()

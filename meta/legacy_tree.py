import json
import os
import matplotlib.pyplot as plt
import networkx as nx

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def build_tree():
    lineage = json.load(open(LINEAGE_PATH))
    G = nx.DiGraph()

    for strat, info in lineage.items():
        parent = info.get("parent", "ROOT")
        model = info.get("model", "unknown")
        node_label = f"{strat}\n{model}"
        G.add_edge(parent, node_label)

    plt.figure(figsize=(18, 12))
    pos = nx.spring_layout(G, k=0.4)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", font_size=7, node_size=1000)
    plt.title("🌳 Strategy Evolution Tree")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    build_tree()
    
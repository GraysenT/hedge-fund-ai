import json
import matplotlib.pyplot as plt
import networkx as nx

LINEAGE = "strategy_memory/strategy_lineage.json"

def build_hypergraph():
    data = json.load(open(LINEAGE))
    G = nx.Graph()

    for strat, info in data.items():
        agent = info.get("proposed_by", "unknown")
        model = info.get("model", "unknown")
        G.add_node(strat, type="strategy")
        G.add_edge(strat, agent, relation="proposed_by")
        G.add_edge(strat, model, relation="model_used")

    colors = ["skyblue" if G.nodes[n].get("type") == "strategy" else "lightgray" for n in G.nodes]
    plt.figure(figsize=(18, 12))
    pos = nx.spring_layout(G, k=0.45)
    nx.draw(G, pos, with_labels=True, node_color=colors, font_size=8)
    plt.title("🧠 Strategy-Agent-Model Hypergraph")
    plt.show()

if __name__ == "__main__":
    build_hypergraph()
    
import networkx as nx
import matplotlib.pyplot as plt

def build_mindmap():
    G = nx.DiGraph()

    G.add_edges_from([
        ("Main System", "Agents"),
        ("Main System", "Strategies"),
        ("Main System", "Models"),
        ("Agents", "Agent Memory"),
        ("Agents", "Agent Voting"),
        ("Agents", "Meta-CEO"),
        ("Strategies", "Plugin Vault"),
        ("Strategies", "Lineage Tracker"),
        ("Models", "LSTM"),
        ("Models", "Transformer"),
        ("Models", "Self-Tuner"),
        ("Main System", "Alpha Firewall"),
        ("Main System", "Trade Journal"),
        ("Main System", "Execution Engine"),
        ("Main System", "Dream Generator"),
        ("Main System", "AI Reflections"),
        ("Main System", "Roadmap Architect"),
        ("Main System", "Governance Proposals"),
    ])

    pos = nx.spring_layout(G, k=0.7)
    plt.figure(figsize=(16, 10))
    nx.draw(G, pos, with_labels=True, node_color="lightyellow", node_size=2000, font_size=10)
    plt.title("🧠 AI Fund Intelligence Mindmap")
    plt.show()

if __name__ == "__main__":
    build_mindmap()
    
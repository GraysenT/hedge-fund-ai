import networkx as nx
import os
import json

GRAPH_PATH = "memory/cognitive_graph.gml"

def build_cognitive_graph():
    G = nx.DiGraph()

    G.add_node("MACD")
    G.add_node("RSI")
    G.add_node("Volume Spike")
    G.add_node("FOMC Event")
    G.add_node("Reversal Alpha")

    G.add_edges_from([
        ("MACD", "Reversal Alpha"),
        ("RSI", "Reversal Alpha"),
        ("Volume Spike", "Reversal Alpha"),
        ("FOMC Event", "Volume Spike")
    ])

    nx.write_gml(G, GRAPH_PATH)
    print("🧠 Cognitive graph built.")

def query_causal_path(target="Reversal Alpha"):
    if not os.path.exists(GRAPH_PATH):
        print("❌ No cognitive graph.")
        return

    G = nx.read_gml(GRAPH_PATH)
    sources = [n for n in G.nodes if G.has_edge(n, target)]
    print(f"🧠 Causal parents of {target}: {sources}")

if __name__ == "__main__":
    build_cognitive_graph()
    query_causal_path()
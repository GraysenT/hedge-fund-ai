import networkx as nx
import matplotlib.pyplot as plt
import json

class StrategyLineageGraph:
    def __init__(self, heritage_file="heritage.json"):
        self.heritage_file = heritage_file
        self.graph = nx.DiGraph()

    def load_heritage(self):
        with open(self.heritage_file, 'r') as f:
            data = json.load(f)
            for child, events in data.items():
                for record in events:
                    parent = record.get("parent")
                    if parent:
                        self.graph.add_edge(parent, child)

    def draw(self):
        self.load_heritage()
        plt.figure(figsize=(10, 6))
        nx.draw(self.graph, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.title("📈 Strategy Lineage Graph")
        plt.show()
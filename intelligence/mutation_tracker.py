import networkx as nx
import matplotlib.pyplot as plt

class MutationGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_mutation(self, parent: str, child: str, score: float):
        self.graph.add_node(child, score=score)
        self.graph.add_edge(parent, child)

    def show(self):
        pos = nx.spring_layout(self.graph)
        scores = [self.graph.nodes[n]["score"] for n in self.graph.nodes]
        nx.draw(self.graph, pos, with_labels=True, node_color=scores, cmap=plt.cm.viridis)
        plt.title("🧬 Strategy Mutation Graph")
        plt.show()
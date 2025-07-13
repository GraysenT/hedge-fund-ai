import networkx as nx
import matplotlib.pyplot as plt

class BeliefGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def assert_belief(self, agent: str, statement: str):
        node = f"{agent} believes: {statement}"
        self.graph.add_node(node)
        self.graph.add_edge(agent, node)

    def add_alignment(self, belief1, belief2):
        self.graph.add_edge(belief1, belief2)

    def visualize(self):
        nx.draw(self.graph, with_labels=True, node_color='lightgreen', font_size=9)
        plt.title("🧠 Inter-Agent Belief Graph")
        plt.show()
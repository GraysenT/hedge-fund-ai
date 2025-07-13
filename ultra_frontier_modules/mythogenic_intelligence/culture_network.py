import networkx as nx


class CultureNetwork:
    def __init__(self):
        self.network = nx.Graph()

    def add_node(self, node, attributes):
        self.network.add_node(node, **attributes)

    def add_edge(self, node1, node2, weight):
        self.network.add_edge(node1, node2, weight=weight)

    def get_cultural_influence(self, node):
        return sum([data['weight'] for _, _, data in self.network.edges(node, data=True)])
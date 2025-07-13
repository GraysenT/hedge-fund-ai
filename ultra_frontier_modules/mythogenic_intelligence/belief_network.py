import networkx as nx


class BeliefNetwork:
    def __init__(self):
        self.network = nx.DiGraph()

    def add_belief(self, belief, influence):
        self.network.add_node(belief, influence=influence)

    def add_influence(self, belief1, belief2, weight):
        self.network.add_edge(belief1, belief2, weight=weight)

    def get_influence(self, belief):
        return sum([data['weight'] for _, _, data in self.network.edges(belief, data=True)])
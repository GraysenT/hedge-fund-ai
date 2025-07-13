import networkx as nx

class SocialCapitalGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def interact(self, agent_a, agent_b, value):
        self.graph.add_edge(agent_a, agent_b, weight=value)

    def top_alliances(self):
        return sorted(self.graph.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)

    def visualize(self):
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight').values()
        nx.draw(self.graph, pos, with_labels=True, width=list(weights))
        plt.title("🤝 Social Capital Graph")
        plt.show()
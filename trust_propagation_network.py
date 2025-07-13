Below is a Python code that models how trust spreads, decays, and rebounds among a network of agents. The model uses a simple graph structure where nodes represent agents and edges represent trust relationships. Trust values are updated based on interactions and time, demonstrating spreading, decaying, and rebounding behaviors.

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class TrustNetwork:
    def __init__(self, num_agents):
        self.graph = nx.DiGraph()
        self.num_agents = num_agents
        self._initialize_agents()

    def _initialize_agents(self):
        for i in range(self.num_agents):
            self.graph.add_node(i, trust=1.0)  # Initial trust level for each agent

    def add_trust_relationship(self, from_agent, to_agent, initial_trust):
        self.graph.add_edge(from_agent, to_agent, trust=initial_trust)

    def update_trust(self, from_agent, to_agent, delta_trust):
        if self.graph.has_edge(from_agent, to_agent):
            current_trust = self.graph[from_agent][to_agent]['trust']
            new_trust = max(0, min(1, current_trust + delta_trust))  # Trust is between 0 and 1
            self.graph[from_agent][to_agent]['trust'] = new_trust

    def decay_trust(self, decay_factor=0.95):
        for from_agent, to_agent in self.graph.edges():
            current_trust = self.graph[from_agent][to_agent]['trust']
            self.graph[from_agent][to_agent]['trust'] = current_trust * decay_factor

    def rebound_trust(self, rebound_factor=1.05, max_trust=1.0):
        for from_agent, to_agent in self.graph.edges():
            current_trust = self.graph[from_agent][to_agent]['trust']
            new_trust = min(max_trust, current_trust * rebound_factor)
            self.graph[from_agent][to_agent]['trust'] = new_trust

    def step(self, decay_factor=0.95, rebound_factor=1.05):
        self.decay_trust(decay_factor)
        self.rebound_trust(rebound_factor)

    def plot_network(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'trust')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', width=1.0, edge_cmap=plt.cm.Blues)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

# Example usage
trust_network = TrustNetwork(5)
trust_network.add_trust_relationship(0, 1, 0.8)
trust_network.add_trust_relationship(1, 2, 0.7)
trust_network.add_trust_relationship(2, 3, 0.9)
trust_network.add_trust_relationship(3, 4, 0.85)
trust_network.add_trust_relationship(4, 0, 0.75)

# Simulate trust dynamics
trust_network.update_trust(0, 1, 0.1)
trust_network.step()
trust_network.plot_network()
```

This code initializes a network of agents with trust relationships and provides functions to update, decay, and rebound trust levels. The `step` function simulates the passage of time affecting trust. The `plot_network` function visualizes the trust relationships and their strengths. Adjust the parameters and relationships as needed to explore different dynamics of trust spread, decay, and rebound.
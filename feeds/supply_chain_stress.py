To detect bottlenecks and macro instability risks from commodity networks, you can use network analysis techniques. Below is a Python script that uses the `networkx` library to create a commodity network graph, identify bottlenecks (using centrality measures), and assess macro instability risks (by evaluating the robustness of the network). This script assumes that the commodity network is represented as a directed graph where nodes represent entities (such as producers, consumers, intermediaries) and edges represent commodity flows between these entities.

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_commodity_network(edges):
    """
    Create a directed graph from a list of edges.
    Each edge is a tuple (source, target, weight).
    """
    G = nx.DiGraph()
    for src, tgt, weight in edges:
        G.add_edge(src, tgt, weight=weight)
    return G

def plot_network(G):
    """
    Plot the network graph.
    """
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def find_bottlenecks(G):
    """
    Identify bottlenecks using betweenness centrality.
    """
    centrality = nx.betweenness_centrality(G, weight='weight')
    # Sort nodes by centrality
    sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    return sorted_centrality

def assess_instability_risk(G):
    """
    Assess macro instability risk by simulating the removal of each node and measuring the impact on the network's connectivity.
    """
    original_size = len(G)
    removal_effects = {}
    for node in G.nodes():
        H = G.copy()
        H.remove_node(node)
        largest_cc = len(max(nx.strongly_connected_components(H), key=len))
        removal_effects[node] = (original_size - largest_cc) / original_size
    sorted_risks = sorted(removal_effects.items(), key=lambda x: x[1], reverse=True)
    return sorted_risks

# Example commodity network edges
edges = [
    ('Producer1', 'Intermediary1', 10),
    ('Intermediary1', 'Consumer1', 5),
    ('Producer2', 'Intermediary2', 15),
    ('Intermediary2', 'Consumer2', 10),
    ('Intermediary1', 'Intermediary2', 8),
    ('Intermediary2', 'Consumer1', 7)
]

# Create and plot the network
G = create_commodity_network(edges)
plot_network(G)

# Find bottlenecks in the network
bottlenecks = find_bottlenecks(G)
print("Bottlenecks (node, centrality):", bottlenecks)

# Assess macro instability risks
instability_risks = assess_instability_risk(G)
print("Instability risks (node, impact):", instability_risks)
```

### Explanation:
1. **Network Creation**: The network is created as a directed graph where nodes are entities and edges are commodity flows with weights.
2. **Plotting**: The network is visualized to help understand its structure.
3. **Bottleneck Detection**: Bottlenecks are detected using betweenness centrality, which identifies nodes that frequently appear on shortest paths between other nodes.
4. **Instability Risk Assessment**: The script simulates the removal of each node to see how it affects the network's connectivity, identifying nodes whose removal leads to significant disconnections.

This script provides a basic framework and can be extended or modified based on specific requirements, such as different types of network analyses or more detailed data attributes.
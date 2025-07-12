Below is a Python script that simulates live mapping to evaluate the risk and confidence associated with each routing decision. This example uses a simple graph-based approach for routing, where nodes represent locations and edges represent paths between them, each with associated risk and confidence levels.

For demonstration purposes, the script uses a static graph, but in a real-world scenario, you could integrate this with live data sources to update the graph dynamically.

```python
import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a graph
G = nx.DiGraph()

# Add nodes and edges with attributes for risk and confidence
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [
    ('A', 'B', {'risk': 0.2, 'confidence': 0.8}),
    ('A', 'C', {'risk': 0.5, 'confidence': 0.6}),
    ('B', 'D', {'risk': 0.1, 'confidence': 0.9}),
    ('C', 'D', {'risk': 0.3, 'confidence': 0.7}),
    ('C', 'E', {'risk': 0.6, 'confidence': 0.5}),
    ('D', 'F', {'risk': 0.2, 'confidence': 0.8}),
    ('E', 'F', {'risk': 0.4, 'confidence': 0.6}),
    ('F', 'G', {'risk': 0.1, 'confidence': 0.9})
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Function to calculate the best path based on a custom metric (e.g., minimizing risk and maximizing confidence)
def best_path(graph, start, end):
    paths = list(nx.all_simple_paths(graph, start, end))
    best_score = float('inf')
    best_path = None
    
    for path in paths:
        risk = sum(graph[u][v]['risk'] for u, v in zip(path[:-1], path[1:]))
        confidence = min(graph[u][v]['confidence'] for u, v in zip(path[:-1], path[1:]))
        score = risk - confidence  # Example metric: lower is better
        
        if score < best_score:
            best_score = score
            best_path = path
            
    return best_path, best_score

# Function to visualize the graph
def visualize_graph(graph, path=None):
    pos = nx.spring_layout(graph)
    edge_labels = {(u, v): f"R:{d['risk']}, C:{d['confidence']}" for u, v, d in graph.edges(data=True)}
    
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='gray')
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title("Routing Decisions: Red edges show the selected path")
    plt.show()

# Example usage
start_node = 'A'
end_node = 'G'
selected_path, path_score = best_path(G, start_node, end_node)
print(f"Selected path: {selected_path} with score: {path_score}")
visualize_graph(G, selected_path)
```

This script does the following:
1. Constructs a directed graph with nodes and edges, where each edge has a risk and confidence attribute.
2. Defines a function `best_path` to find the optimal path from a start to an end node based on a simple scoring mechanism that attempts to minimize risk and maximize confidence.
3. Defines a function `visualize_graph` to visualize the graph and the selected path.
4. Uses these functions to compute and visualize the best path from node 'A' to node 'G'.

You can adapt this script to handle more complex scenarios, integrate real-time data updates, or use more sophisticated algorithms for pathfinding and risk/confidence evaluation.
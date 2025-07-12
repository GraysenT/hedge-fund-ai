Below is a Python script that simulates building and testing alternate timelines for system development and signal routing. The script uses a simple model where each timeline represents a different configuration of signal paths in a network system. The script will generate random network configurations, simulate signal routing, and evaluate the performance of each configuration.

```python
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_network(num_nodes, num_edges):
    """
    Generates a random network graph.
    """
    G = nx.gnm_random_graph(num_nodes, num_edges)
    return G

def simulate_signal_routing(G, source, target):
    """
    Simulates signal routing from source to target in the network graph G.
    Returns the path if exists, otherwise None.
    """
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return None

def evaluate_network(G, num_tests=100):
    """
    Evaluates the network by performing multiple tests of signal routing.
    Returns the success rate of signal routing.
    """
    success_count = 0
    nodes = list(G.nodes)
    
    for _ in range(num_tests):
        source, target = random.sample(nodes, 2)
        if simulate_signal_routing(G, source, target) is not None:
            success_count += 1
    
    return success_count / num_tests

def main():
    num_nodes = 10
    num_edges = 15
    num_timelines = 5
    evaluation_results = []
    
    # Generate and test multiple timelines
    for i in range(num_timelines):
        G = generate_network(num_nodes, num_edges)
        success_rate = evaluate_network(G)
        evaluation_results.append((G, success_rate))
        
        # Plotting the network
        plt.figure(figsize=(8, 5))
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.title(f"Timeline {i+1} - Success Rate: {success_rate:.2f}")
        plt.show()
    
    # Print the results
    for idx, (G, rate) in enumerate(evaluation_results):
        print(f"Timeline {idx+1}: Success Rate = {rate:.2f}")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Network Generation**: The `generate_network` function creates a random graph with a specified number of nodes and edges using the NetworkX library.

2. **Signal Routing Simulation**: The `simulate_signal_routing` function attempts to find the shortest path between a source and a target node in the graph. If a path exists, it returns the path; otherwise, it returns `None`.

3. **Network Evaluation**: The `evaluate_network` function tests the network by attempting to route signals between randomly chosen pairs of nodes multiple times. It calculates the success rate based on how often a valid path is found.

4. **Main Function**: The script generates multiple network configurations (timelines), evaluates each, and plots them. It then prints the success rates of signal routing for each timeline.

5. **Visualization**: Each network configuration is visualized using matplotlib to show how the network topology looks for each timeline.

This script can be extended or modified to include more complex network configurations, different types of evaluations, or more detailed simulations based on specific requirements.
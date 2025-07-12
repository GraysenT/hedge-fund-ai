Below is a Python script that uses `matplotlib` and `networkx` to create a dynamic graph view of module and agent trust relationships over time. The script simulates trust relationships using a simple model and updates the graph at each time step to reflect changes in these relationships.

```python
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation

# Parameters
num_agents = 10
num_modules = 5
num_steps = 50
update_interval = 500  # milliseconds

# Create a directed graph
G = nx.DiGraph()

# Adding nodes for agents and modules
agent_nodes = [f"Agent {i+1}" for i in range(num_agents)]
module_nodes = [f"Module {i+1}" for i in range(num_modules)]
G.add_nodes_from(agent_nodes, type='agent')
G.add_nodes_from(module_nodes, type='module')

# Initialize random trust relationships
trust_values = np.random.rand(num_agents, num_modules)

# Function to update the graph
def update_graph(num):
    # Simulate changes in trust relationships
    trust_values[:] += (np.random.rand(num_agents, num_modules) - 0.5) * 0.1
    np.clip(trust_values, 0, 1, out=trust_values)

    # Clear existing edges
    G.remove_edges_from(list(G.edges()))

    # Add edges with updated trust values
    for i, agent in enumerate(agent_nodes):
        for j, module in enumerate(module_nodes):
            if trust_values[i, j] > 0.2:  # Only show significant trust relationships
                G.add_edge(agent, module, weight=trust_values[i, j])

    # Clear the plot and redraw
    plt.cla()
    pos = nx.spring_layout(G, seed=42)  # Layout for nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', nodelist=agent_nodes)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightgreen', nodelist=module_nodes)
    nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray', width=2,
                                   edge_cmap=plt.cm.Blues, edge_vmin=0, edge_vmax=1)

    # Set edge color based on trust value
    edge_colors = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color=edge_colors,
                           edge_cmap=plt.cm.Blues, width=2)

    plt.title('Module and Agent Trust Relationships Over Time')
    plt.box(False)

# Set up plot
fig, ax = plt.subplots(figsize=(10, 8))
plt.axis('off')

# Create animation
ani = animation.FuncAnimation(fig, update_graph, frames=num_steps, interval=update_interval, repeat=True)

plt.show()
```

### Explanation:
1. **Graph Initialization**: The script initializes a directed graph with nodes representing agents and modules.
2. **Random Trust Relationships**: Initial trust values between agents and modules are set randomly.
3. **Update Function**: This function is called for each frame in the animation. It updates the trust values, modifies the graph edges based on these values, and redraws the graph.
4. **Animation**: `matplotlib.animation.FuncAnimation` is used to animate the graph, showing how relationships evolve over time.

### Requirements:
- Python libraries: `matplotlib`, `networkx`, `numpy`
- This script assumes a simple model where trust values are updated randomly. In a real-world scenario, you would update these based on actual data or a more sophisticated model.
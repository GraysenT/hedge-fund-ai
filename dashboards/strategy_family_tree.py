Below is a Python script that uses `matplotlib` and `networkx` to create an interactive evolution tree of strategy branches. This script will generate a simple tree structure representing different strategies and their evolution over time. The interactivity allows you to click on nodes to see more information about each strategy.

```python
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the class to handle the interactive part of the tree
class InteractiveStrategyTree:
    def __init__(self, graph, pos):
        self.graph = graph
        self.pos = pos
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.draw_graph()

    def draw_graph(self):
        nx.draw(self.graph, pos=self.pos, with_labels=True, ax=self.ax, picker=True, node_size=700, node_color='lightblue')
        plt.show()

    def on_pick(self, event):
        node = event.artist
        node_idx = node.get_url()
        strategy_info = self.graph.nodes[node_idx]['info']
        
        # Clear the previous annotations
        self.ax.clear()
        self.draw_graph()
        
        # Add annotation
        self.ax.annotate(f"Strategy Info: {strategy_info}",
                         xy=self.pos[node_idx],
                         xytext=(10, 10),
                         textcoords='offset points',
                         arrowprops=dict(facecolor='black', shrink=0.05),
                         bbox=dict(boxstyle="round,pad=0.5", fc="yellow", ec="b", lw=2))
        plt.draw()

def create_strategy_graph():
    G = nx.DiGraph()

    # Adding nodes with some example strategies
    strategies = {
        'S0': 'Initial Strategy',
        'S1': 'Developed Strategy 1',
        'S2': 'Developed Strategy 2',
        'S3': 'Refined Strategy 1',
        'S4': 'Alternative Strategy 1',
        'S5': 'Final Strategy'
    }

    for key, value in strategies.items():
        G.add_node(key, info=value)

    # Connecting nodes to form a tree
    edges = [('S0', 'S1'), ('S0', 'S2'), ('S1', 'S3'), ('S2', 'S4'), ('S3', 'S5'), ('S4', 'S5')]
    G.add_edges_from(edges)

    # Position nodes for better visualization
    pos = nx.spring_layout(G)
    return G, pos

# Main function to run the interactive tree
if __name__ == '__main__':
    G, pos = create_strategy_graph()
    tree = InteractiveStrategyTree(G, pos)
```

### Explanation:
1. **InteractiveStrategyTree Class**: This class handles the creation and interaction of the strategy tree. It initializes the graph, sets up a matplotlib figure, and connects a pick event for interactivity.
2. **create_strategy_graph Function**: This function creates a directed graph using `networkx`, adds nodes and edges to represent strategies and their relationships, and returns the graph and positions of the nodes.
3. **Main Execution Block**: This part initializes the graph and runs the interactive visualization.

### Requirements:
- You need to have `matplotlib` and `networkx` installed in your Python environment. You can install them via pip:
  ```bash
  pip install matplotlib networkx
  ```

This script provides a basic framework for an interactive evolution tree of strategies. You can expand it by adding more complex strategies, additional details in the nodes, or enhancing the interactivity.
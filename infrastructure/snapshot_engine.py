Below is a Python script that demonstrates how to take recursive snapshots of system state, memory usage, and a simple logic graph representation. This script uses the `psutil` library for system and memory information, and `networkx` along with `matplotlib` for creating and visualizing a logic graph.

First, ensure you have the necessary libraries installed:
```bash
pip install psutil networkx matplotlib
```

Here's the Python script:

```python
import psutil
import networkx as nx
import matplotlib.pyplot as plt
import time
import os

def snapshot_system_state():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    # Get Memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    return cpu_usage, memory_usage

def create_logic_graph():
    G = nx.DiGraph()
    G.add_edges_from([
        ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')
    ])
    return G

def draw_logic_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='#FF5733', node_size=700, font_size=15)
    plt.show()

def recursive_snapshot(interval, depth):
    if depth == 0:
        return
    cpu, mem = snapshot_system_state()
    print(f"Snapshot at depth {depth}: CPU Usage: {cpu}%, Memory Usage: {mem}%")
    
    G = create_logic_graph()
    draw_logic_graph(G)
    
    time.sleep(interval)
    recursive_snapshot(interval, depth - 1)

def main():
    interval = 5  # seconds
    depth = 3  # How deep the recursion goes
    recursive_snapshot(interval, depth)

if __name__ == "__main__":
    main()
```

### Explanation:
- **snapshot_system_state()**: This function fetches the current CPU and memory usage using `psutil`.
- **create_logic_graph()**: Creates a simple directed graph using `networkx` to simulate a logic graph.
- **draw_logic_graph(G)**: Visualizes the graph using `matplotlib`.
- **recursive_snapshot(interval, depth)**: This function recursively takes snapshots of the system state and visualizes the logic graph. It decrements the depth each time until it reaches zero.
- **main()**: Sets the interval between snapshots and the depth of recursion, then starts the recursive snapshot process.

This script will take snapshots of the system state and visualize a predefined logic graph at specified intervals, decreasing the recursion depth each time until it stops. Adjust the `interval` and `depth` in the `main()` function as needed.
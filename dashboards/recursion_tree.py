from strategies.lineage_tracker import get_lineage_graph
import networkx as nx
import matplotlib.pyplot as plt

def show_tree():
    G = get_lineage_graph()
    nx.draw(G, with_labels=True)
    plt.title("Strategy Lineage")
    plt.show()
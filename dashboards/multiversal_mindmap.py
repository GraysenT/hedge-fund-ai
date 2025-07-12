import matplotlib.pyplot as plt

class MultiversalMindmap:
    def __init__(self):
        self.universes = []
    
    def add_universe(self, universe_name):
        """View evolving universes, agents, and recursive cycles."""
        self.universes.append(universe_name)
        print(f"Added universe: {universe_name}")
    
    def plot_mindmap(self):
        """Visualize universes in a mindmap-like structure."""
        plt.figure(figsize=(10, 10))
        plt.title("Multiversal Mindmap")
        plt.scatter(range(len(self.universes)), [1] * len(self.universes), label=self.universes)
        plt.legend()
        plt.show()
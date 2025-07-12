import matplotlib.pyplot as plt

class StrategyEvolutionDashboard:
    def __init__(self):
        self.strategies = []

    def track_strategy(self, strategy_name, performance):
        """Track the evolution of strategies and their performance."""
        self.strategies.append({"strategy": strategy_name, "performance": performance})
        print(f"Tracked strategy: {strategy_name} with performance: {performance}")
    
    def visualize_strategy_evolution(self):
        """Visualize the evolution of strategies and their performance."""
        plt.figure(figsize=(10, 5))
        plt.title("Strategy Evolution")
        strategy_names = [entry["strategy"] for entry in self.strategies]
        performances = [entry["performance"] for entry in self.strategies]
        plt.plot(strategy_names, performances, label='Strategy Performance')
        plt.xlabel("Strategy")
        plt.ylabel("Performance")
        plt.legend()
        plt.show()
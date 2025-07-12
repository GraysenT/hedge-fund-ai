class MetaStrategyDashboard:
    def __init__(self):
        self.meta_strategies = []

    def track_meta_strategy(self, strategy_name, goal):
        """Track meta-strategy performance and goals."""
        self.meta_strategies.append({"strategy_name": strategy_name, "goal": goal})
        print(f"Tracked meta-strategy: {strategy_name} with goal: {goal}")
    
    def visualize_meta_strategies(self):
        """Visualize meta-strategy performance and optimization."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Meta-Strategy Optimization")
        strategy_names = [entry["strategy_name"] for entry in self.meta_strategies]
        goals = [entry["goal"] for entry in self.meta_strategies]
        plt.bar(strategy_names, goals)
        plt.xlabel("Meta-Strategy")
        plt.ylabel("Goal Achievement")
        plt.show()
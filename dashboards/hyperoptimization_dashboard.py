class HyperoptimizationDashboard:
    def __init__(self):
        self.optimization_data = []

    def track_optimization(self, strategy_name, optimization_factor):
        """Track recursive optimization strategies across domains."""
        self.optimization_data.append({"strategy_name": strategy_name, "optimization_factor": optimization_factor})
        print(f"Tracked optimization: {strategy_name} with factor: {optimization_factor}")
    
    def visualize_optimization(self):
        """Visualize the optimization process across recursive strategies."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Recursive Hyperoptimization")
        strategies = [entry["strategy_name"] for entry in self.optimization_data]
        factors = [entry["optimization_factor"] for entry in self.optimization_data]
        plt.bar(strategies, factors)
        plt.xlabel("Strategy")
        plt.ylabel("Optimization Factor")
        plt.show()
class SelfOptimizationDashboard:
    def __init__(self):
        self.optimization_log = []

    def track_optimization(self, optimization_name, factor):
        """Track the system's self-optimization progress."""
        self.optimization_log.append({"optimization_name": optimization_name, "factor": factor})
        print(f"Tracked optimization: {optimization_name} with factor: {factor}")
    
    def visualize_optimization(self):
        """Visualize the system's optimization progress."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Self Optimization Progress")
        optimizations = [entry["optimization_name"] for entry in self.optimization_log]
        factors = [entry["factor"] for entry in self.optimization_log]
        plt.bar(optimizations, factors)
        plt.xlabel("Optimization")
        plt.ylabel("Factor")
        plt.show()
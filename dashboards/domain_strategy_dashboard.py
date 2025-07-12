class DomainStrategyDashboard:
    def __init__(self):
        self.strategies = []

    def track_domain_strategy(self, strategy_name, domain, optimization_factor):
        """Track the evolution of strategies across multiple domains."""
        self.strategies.append({"strategy_name": strategy_name, "domain": domain, "optimization_factor": optimization_factor})
        print(f"Tracked strategy: {strategy_name} in domain: {domain} with optimization factor: {optimization_factor}")
    
    def visualize_domain_strategies(self):
        """Visualize strategy performance across multiple domains."""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.title("Domain Strategy Optimization")
        strategy_names = [entry["strategy_name"] for entry in self.strategies]
        optimization_factors = [entry["optimization_factor"] for entry in self.strategies]
        plt.bar(strategy_names, optimization_factors)
        plt.xlabel("Strategy Name")
        plt.ylabel("Optimization Factor")
        plt.show()
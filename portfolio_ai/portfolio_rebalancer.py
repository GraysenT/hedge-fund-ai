class PortfolioRebalancer:
    def __init__(self):
        self.current_allocations = {}

    def rebalance(self, new_allocations):
        print("[REBALANCE] Rebalancing portfolio...")
        for strategy, weight in new_allocations.items():
            old = self.current_allocations.get(strategy, 0)
            delta = round(weight - old, 4)
            print(f" - {strategy}: {old:.2f} → {weight:.2f} (Δ {delta:+.2f})")
        self.current_allocations = new_allocations
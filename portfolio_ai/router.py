class PortfolioRouter:
    def __init__(self):
        self.routes = {}

    def set_allocation(self, strategy, weight):
        self.routes[strategy] = weight

    def get_allocation(self, strategy):
        return self.routes.get(strategy, 0.0)

    def route_signal(self, signal):
        strategy = signal.get("strategy")
        weight = self.get_allocation(strategy)
        signal["allocated_confidence"] = round(signal["confidence"] * weight, 3)
        return signal

    def full_allocation(self):
        return self.routes
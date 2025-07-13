import random

class MarketScout:
    def __init__(self, known_markets: list):
        self.known = set(known_markets)
        self.available = ["AAPL", "TSLA", "ETHUSD", "NZDJPY", "SP500", "NATGAS", "ADA", "SOL", "XAUUSD"]

    def explore(self):
        new_markets = [m for m in self.available if m not in self.known]
        discovered = random.sample(new_markets, k=min(2, len(new_markets)))
        for m in discovered:
            self.known.add(m)
        return discovered
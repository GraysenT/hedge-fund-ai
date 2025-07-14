class LiveFeed:
    def __init__(self, symbol="ETHUSD"):
        self.symbol = symbol

    def fetch(self):
        # Placeholder for real-time price API
        return {
            "price": 1800.0,
            "ma": 1750.0
        }
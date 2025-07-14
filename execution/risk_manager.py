class RiskManager:
    def __init__(self, max_risk=0.05):
        self.max_risk = max_risk  # e.g., 5% of capital

    def calculate_position_size(self, capital, price):
        if price == 0:
            return 0
        size = (capital * self.max_risk) / price
        return max(0, round(size, 4))

    def validate_trade(self, signal, position, capital):
        if signal not in ["buy", "sell", "hold"]:
            return False
        if capital <= 0:
            return False
        return True
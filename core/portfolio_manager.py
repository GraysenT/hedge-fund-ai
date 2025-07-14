from typing import Dict

class PortfolioManager:
    def __init__(self):
        self.positions = {}
        self.cash = 1000000  # initial capital

    def update_position(self, symbol: str, action: str, size: float, price: float):
        if action == "buy":
            self.positions[symbol] = self.positions.get(symbol, 0) + size
            self.cash -= size * price
        elif action == "sell":
            self.positions[symbol] = self.positions.get(symbol, 0) - size
            self.cash += size * price

    def get_exposure(self) -> Dict:
        return {"positions": self.positions, "cash": self.cash}
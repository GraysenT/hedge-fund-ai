import uuid
import random

class BusinessSeed:
    def __init__(self, vision: str, capital: float = 1000.0):
        self.id = str(uuid.uuid4())
        self.vision = vision
        self.capital = capital
        self.success = 0.0
        self.growth_bias = random.uniform(0.8, 1.2)
        self.volatility = random.uniform(0.1, 0.5)

    def simulate_tick(self, market_pulse: float):
        delta = market_pulse * self.growth_bias
        noise = random.gauss(0, self.volatility)
        gain = delta + noise
        self.capital += gain
        self.success = max(self.success, self.capital)
        return gain
    
    def get_signal(self):
        if self.capital > 1100:
            return "buy"
        elif self.capital < 900:
            return "sell"
        return "hold"
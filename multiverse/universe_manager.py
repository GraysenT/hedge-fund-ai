import random

class MarketUniverse:
    def __init__(self, name, gravity, volatility_bias, liquidity_level):
        self.name = name
        self.gravity = gravity  # pull toward mean
        self.volatility_bias = volatility_bias  # higher = more chaotic
        self.liquidity_level = liquidity_level  # affects slippage
        self.agents = []

    def simulate_tick(self):
        for agent in self.agents:
            market_shift = random.gauss(self.gravity, self.volatility_bias)
            profit = market_shift * agent.get_risk_bias()
            agent.capital += profit * (1 - (1 - self.liquidity_level))

    def add_agent(self, agent):
        self.agents.append(agent)
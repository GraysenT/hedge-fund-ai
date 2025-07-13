from .universe_agent import UniverseAgent
import random

class SimulationWorld:
    def __init__(self):
        self.agents = []
        self.market_state = {"volatility": 0.2, "trend": 0.5}

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        results = []
        for agent in self.agents:
            action = agent.act(self.market_state)
            pnl = self.evaluate_action(agent, action)
            result = {
                "pnl": pnl,
                "reputation_change": pnl / agent.capital,
                "action": action
            }
            agent.update_state(result)
            results.append(result)
        self.randomly_shift_market()
        return results

    def evaluate_action(self, agent, action):
        # Mock reward logic: small gain or loss depending on action and volatility
        multiplier = random.uniform(-0.03, 0.05)
        return round(agent.capital * multiplier, 2)

    def randomly_shift_market(self):
        self.market_state["volatility"] += random.uniform(-0.01, 0.01)
        self.market_state["trend"] += random.uniform(-0.05, 0.05)
        self.market_state["volatility"] = round(max(0, min(1, self.market_state["volatility"])), 3)
        self.market_state["trend"] = round(max(0, min(1, self.market_state["trend"])), 3)
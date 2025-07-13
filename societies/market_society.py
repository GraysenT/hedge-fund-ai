from random import choice, uniform

class MarketSociety:
    def __init__(self, market):
        self.market = market
        self.agents = {}
        self.laws = {
            "max_risk": 0.1,
            "mutation_rate": 0.05,
            "resource_tax": 0.02
        }

    def register_agent(self, name, strategy):
        self.agents[name] = {"strategy": strategy, "capital": 1000.0, "karma": 0.0}

    def govern(self):
        # Agents violating risk threshold lose karma
        for name, agent in self.agents.items():
            if uniform(0, 1) > (1 - self.laws["max_risk"]):
                agent["karma"] -= 1

    def evolve_policy(self):
        # Random mutation of laws
        self.laws["mutation_rate"] += uniform(-0.01, 0.01)
        self.laws["mutation_rate"] = max(0, min(1, self.laws["mutation_rate"]))
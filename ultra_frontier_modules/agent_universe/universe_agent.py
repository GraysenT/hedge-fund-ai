import uuid
import random

class UniverseAgent:
    def __init__(self, name, strategy_profile, initial_capital):
        self.id = str(uuid.uuid4())
        self.name = name
        self.profile = strategy_profile
        self.capital = initial_capital
        self.reputation = 0.5
        self.memory = []

    def act(self, environment_state):
        """
        Make a decision based on environment (e.g., 'buy', 'sell', 'hold').
        This can be expanded into complex strategy logic.
        """
        move = random.choice(["buy", "sell", "hold"])
        amount = random.uniform(0.01, 0.1) * self.capital
        return {"agent": self.name, "action": move, "amount": round(amount, 2)}

    def update_state(self, result):
        self.capital += result.get("pnl", 0)
        self.reputation += result.get("reputation_change", 0)
        self.reputation = max(0, min(1, self.reputation))
        self.memory.append(result)
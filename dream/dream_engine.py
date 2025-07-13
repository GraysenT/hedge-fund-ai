import random

class DreamEngine:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.dreams = []

    def dream_tick(self, context: dict):
        future_price = context["price"] * random.uniform(0.95, 1.10)
        imagined_outcome = "profit" if future_price > context["price"] else "loss"
        dream = {
            "future_price": future_price,
            "context": context,
            "imagined_outcome": imagined_outcome
        }
        self.dreams.append(dream)
        return dream
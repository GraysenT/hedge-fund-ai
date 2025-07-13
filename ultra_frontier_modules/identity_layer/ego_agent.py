import uuid
import random

class EgoAgent:
    def __init__(self, name, identity_type="analytical", conviction=0.5, volatility=0.3):
        self.id = str(uuid.uuid4())
        self.name = name
        self.identity_type = identity_type
        self.conviction = conviction      # 0–1: how strongly it believes in itself
        self.volatility = volatility      # 0–1: how easily it changes belief
        self.beliefs = {}

    def update_belief(self, topic, new_value, signal_strength):
        prior = self.beliefs.get(topic, 0.5)
        adjustment = (signal_strength - 0.5) * (1 - self.volatility)
        updated = prior + adjustment * self.conviction
        self.beliefs[topic] = round(min(max(updated, 0), 1), 3)

    def express_opinion(self, topic):
        return {
            "Agent": self.name,
            "Identity": self.identity_type,
            "Topic": topic,
            "Belief": self.beliefs.get(topic, 0.5)
        }

    def profile(self):
        return {
            "Name": self.name,
            "Type": self.identity_type,
            "Conviction": self.conviction,
            "Volatility": self.volatility,
            "Beliefs": self.beliefs
        }
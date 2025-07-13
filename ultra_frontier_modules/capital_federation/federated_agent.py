import uuid
import random

class FederatedAgent:
    def __init__(self, name, base_capital, strategy_type, trust_score=0.5):
        self.id = str(uuid.uuid4())
        self.name = name
        self.capital = base_capital
        self.strategy = strategy_type
        self.trust_score = trust_score
        self.performance = []
        self.votes = []

    def update_performance(self, pnl):
        self.performance.append(pnl)
        if len(self.performance) > 10:
            self.performance.pop(0)

    def vote_on_proposal(self, proposal_id, signal_strength):
        vote = {
            "proposal_id": proposal_id,
            "vote_weight": signal_strength * self.trust_score,
            "agent": self.name
        }
        self.votes.append(vote)
        return vote

    def current_score(self):
        if not self.performance:
            return self.trust_score
        return round(sum(self.performance[-5:]) / len(self.performance[-5:]), 3)
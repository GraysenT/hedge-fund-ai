from .federated_agent import FederatedAgent
import random

class CapitalFederation:
    def __init__(self):
        self.agents = []
        self.proposals = {}
        self.votes = {}

    def register_agent(self, agent):
        self.agents.append(agent)

    def propose_allocation(self, id, description, capital_amount):
        self.proposals[id] = {
            "id": id,
            "description": description,
            "amount": capital_amount,
            "votes": []
        }

    def broadcast_vote_request(self, proposal_id):
        signal_strength = random.uniform(0.5, 1.0)
        for agent in self.agents:
            vote = agent.vote_on_proposal(proposal_id, signal_strength)
            self.proposals[proposal_id]["votes"].append(vote)

    def resolve_proposal(self, proposal_id):
        votes = self.proposals[proposal_id]["votes"]
        total = sum(v["vote_weight"] for v in votes)
        decision = "PASS" if total > len(self.agents) * 0.5 else "FAIL"
        return {
            "proposal": self.proposals[proposal_id],
            "total_vote_weight": round(total, 3),
            "decision": decision
        }
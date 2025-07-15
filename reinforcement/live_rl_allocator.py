import random

class RLAllocator:
    def __init__(self, agents):
        self.agents = agents
        self.q_table = {a.id: 0.5 for a in agents}  # Init Q values

    def choose_allocation(self):
        total_q = sum(self.q_table.values())
        return {k: v / total_q for k, v in self.q_table.items()}

    def reward(self, agent_id, pnl):
        self.q_table[agent_id] += 0.01 * pnl  # simple reward shaping
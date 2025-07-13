import copy

class ForkingSimulator:
    def __init__(self):
        self.universes = []

    def fork(self, agent_state, market_state):
        forked_agent = copy.deepcopy(agent_state)
        forked_market = copy.deepcopy(market_state)
        sim_id = f"sim_{len(self.universes)}"
        self.universes.append((sim_id, forked_agent, forked_market))
        print(f"🌱 Forked new simulation branch: {sim_id}")
        return sim_id
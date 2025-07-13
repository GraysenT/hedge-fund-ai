import random

class VirtualAgent:
    def __init__(self, name):
        self.name = name
        self.capital = 1000
        self.strategy = random.choice(["trend", "mean", "ml"])
        self.karma = 0

    def act(self):
        outcome = random.uniform(-1, 2)
        self.capital += outcome * 10
        self.karma += 1 if outcome > 0 else -1

def run_simulation(agent_count=1000, cycles=50):
    agents = [VirtualAgent(f"agent_{i}") for i in range(agent_count)]
    for _ in range(cycles):
        for a in agents:
            a.act()
    top = sorted(agents, key=lambda a: a.capital, reverse=True)[:5]
    return [(a.name, a.capital, a.strategy, a.karma) for a in top]
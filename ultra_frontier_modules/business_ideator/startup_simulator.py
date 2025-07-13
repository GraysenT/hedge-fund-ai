import random
import uuid

class SimulatedStartup:
    def __init__(self, name, domain, funding, founder_ai_score):
        self.id = uuid.uuid4()
        self.name = name
        self.domain = domain
        self.funding = funding
        self.ai_score = founder_ai_score
        self.success_chance = self.evaluate()

    def evaluate(self):
        return round((self.ai_score * 0.6 + random.random() * 0.4) * (self.funding / 1e6), 3)

def simulate_startups(n=5):
    ideas = ["climate analytics", "on-demand logistics", "AI therapy", "precision farming", "legal GPT agent"]
    startups = []
    for _ in range(n):
        name = f"{random.choice(['Neo', 'Quantum', 'Atlas', 'Bright'])}{random.randint(100,999)}"
        startup = SimulatedStartup(name, random.choice(ideas), random.randint(1, 10) * 1e6, random.uniform(0.5, 1.0))
        startups.append(vars(startup))
    return startups

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_startups(10))
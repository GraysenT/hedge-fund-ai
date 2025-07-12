```python
import numpy as np

class Agent:
    def __init__(self, name):
        self.name = name
        self.decisions = []
        self.external_guidance = []

    def make_decision(self, decision, guided=False):
        self.decisions.append(decision)
        self.external_guidance.append(guided)

    def calculate_self_guidance_score(self):
        if not self.decisions:
            return 0
        total_decisions = len(self.decisions)
        self_guided_decisions = total_decisions - sum(self.external_guidance)
        return self_guided_decisions / total_decisions

# Example usage
agent1 = Agent("Agent1")
agent1.make_decision("Move forward")
agent1.make_decision("Turn left", guided=True)
agent1.make_decision("Pick up object")

agent2 = Agent("Agent2")
agent2.make_decision("Move forward", guided=True)
agent2.make_decision("Turn right", guided=True)

print(f"{agent1.name} Self-Guidance Score: {agent1.calculate_self_guidance_score():.2f}")
print(f"{agent2.name} Self-Guidance Score: {agent2.calculate_self_guidance_score():.2f}")
```
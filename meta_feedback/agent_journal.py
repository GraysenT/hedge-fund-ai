```python
import json

class Agent:
    def __init__(self, name):
        self.name = name
        self.thoughts = []
        self.scores = []
        self.regrets = []
        self.survival_status = True

    def log_thought(self, thought):
        self.thoughts.append(thought)

    def log_score(self, score):
        self.scores.append(score)

    def log_regret(self, regret):
        self.regrets.append(regret)

    def update_survival_status(self, status):
        self.survival_status = status

    def get_summary(self):
        return {
            "name": self.name,
            "thoughts": self.thoughts,
            "scores": self.scores,
            "regrets": self.regrets,
            "survival_status": self.survival_status
        }

    def save_logs(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.get_summary(), file, indent=4)

# Example usage
agent = Agent("Agent_01")
agent.log_thought("I should move cautiously.")
agent.log_score(10)
agent.log_regret("Didn't explore the east side.")
agent.update_survival_status(False)

# Save agent's logs to a file
agent.save_logs("agent_01_logs.json")
```
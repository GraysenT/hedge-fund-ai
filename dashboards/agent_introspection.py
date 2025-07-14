```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.thoughts = []
        self.regret_logs = []
        self.purpose = "Learning"

    def think(self, thought):
        self.thoughts.append(thought)
        self.recursive_thinking(thought, 3)  # Recursive depth of 3

    def recursive_thinking(self, thought, depth):
        if depth > 0:
            new_thought = f"Reconsidering {thought}"
            self.thoughts.append(new_thought)
            self.recursive_thinking(new_thought, depth - 1)

    def log_regret(self, regret):
        self.regret_logs.append(regret)

    def evolve_purpose(self, new_purpose):
        self.purpose = new_purpose

    def __str__(self):
        return (f"Agent: {self.name}\n"
                f"Purpose: {self.purpose}\n"
                f"Thoughts: {self.thoughts}\n"
                f"Regrets: {self.regret_logs}\n")

# Example usage
if __name__ == "__main__":
    agent = Agent("AI-42")
    agent.think("Should I improve my algorithms?")
    agent.log_regret("Not optimizing the recursive function earlier.")
    agent.evolve_purpose("Enhancing AI capabilities")

    print(agent)
```
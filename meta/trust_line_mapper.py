Below is a Python code example that implements a simple system for tracking trust lineage across agents and modules through promotion and degradation mechanisms. This system uses classes to represent agents and modules, and it manages trust levels based on interactions or evaluations.

```python
class Agent:
    def __init__(self, name, trust_level=0):
        self.name = name
        self.trust_level = trust_level
        self.history = []

    def promote(self, amount):
        self.trust_level += amount
        self.history.append((amount, "Promotion"))

    def degrade(self, amount):
        self.trust_level -= amount
        self.history.append((-amount, "Degradation"))

    def get_trust_level(self):
        return self.trust_level

    def get_history(self):
        return self.history

class Module:
    def __init__(self, identifier):
        self.identifier = identifier
        self.agents = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent

    def evaluate_agent(self, agent_name, result):
        if agent_name in self.agents:
            if result == "positive":
                self.agents[agent_name].promote(10)
            elif result == "negative":
                self.agents[agent_name].degrade(5)

    def get_agent_trust(self, agent_name):
        if agent_name in self.agents:
            return self.agents[agent_name].get_trust_level()
        else:
            return None

    def get_agent_history(self, agent_name):
        if agent_name in self.agents:
            return self.agents[agent_name].get_history()
        else:
            return None

# Example usage
agent1 = Agent("Alice")
agent2 = Agent("Bob")

module1 = Module("Module1")
module1.add_agent(agent1)
module1.add_agent(agent2)

module1.evaluate_agent("Alice", "positive")
module1.evaluate_agent("Bob", "negative")

print("Alice's Trust Level:", module1.get_agent_trust("Alice"))
print("Bob's Trust Level:", module1.get_agent_trust("Bob"))

print("Alice's History:", module1.get_agent_history("Alice"))
print("Bob's History:", module1.get_agent_history("Bob"))
```

This code defines two classes, `Agent` and `Module`. Agents have a trust level that can be modified by promotions or degradations, which are recorded in their history. Modules manage multiple agents and can evaluate them, affecting their trust levels based on the results of these evaluations. The example usage demonstrates adding agents to a module, evaluating them, and then retrieving their trust levels and histories.
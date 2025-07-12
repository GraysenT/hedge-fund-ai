```python
class Agent:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def make_decision(self, context):
        # Placeholder for decision-making logic
        return f"{self.name} decides based on {context}"

class AgentCoordinator:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)
        # Sort agents by priority, higher priority first
        self.agents.sort(key=lambda x: x.priority, reverse=True)

    def make_decision(self, context):
        for agent in self.agents:
            decision = agent.make_decision(context)
            if decision:
                return decision
        return "No decision made"

# Example usage
if __name__ == "__main__":
    coordinator = AgentCoordinator()
    agent1 = Agent("Agent1", 1)
    agent2 = Agent("Agent2", 2)
    agent3 = Agent("Agent3", 3)

    coordinator.register_agent(agent1)
    coordinator.register_agent(agent2)
    coordinator.register_agent(agent3)

    decision_context = "current situation"
    decision = coordinator.make_decision(decision_context)
    print(decision)
```
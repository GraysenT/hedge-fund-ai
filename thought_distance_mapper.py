Here's a Python code that implements a basic model to map cognitive distance between agents based on their ideas and strategies using recursive memory. This example uses a simple approach where each agent has a set of ideas and strategies, and cognitive distance is calculated based on the similarity of these attributes. Recursive memory is simulated by allowing agents to update their ideas and strategies based on past interactions.

```python
import numpy as np

class Agent:
    def __init__(self, id, ideas, strategies):
        self.id = id
        self.ideas = np.array(ideas)
        self.strategies = np.array(strategies)
        self.memory = []

    def update_ideas(self, other_ideas):
        # Simple model: average the current ideas with the ideas from another agent
        self.ideas = (self.ideas + other_ideas) / 2

    def update_strategies(self, other_strategies):
        # Simple model: average the current strategies with the strategies from another agent
        self.strategies = (self.strategies + other_strategies) / 2

    def remember_interaction(self, other):
        # Store a simple record of interaction
        self.memory.append((other.id, other.ideas.copy(), other.strategies.copy()))

    def interact(self, other):
        self.remember_interaction(other)
        other.remember_interaction(self)
        self.update_ideas(other.ideas)
        self.update_strategies(other.strategies)

def cognitive_distance(agent1, agent2):
    # Calculate cognitive distance as Euclidean distance between ideas and strategies
    ideas_distance = np.linalg.norm(agent1.ideas - agent2.ideas)
    strategies_distance = np.linalg.norm(agent1.strategies - agent2.strategies)
    return ideas_distance + strategies_distance

# Example usage
agent1 = Agent(1, [1, 2, 3], [3, 2, 1])
agent2 = Agent(2, [2, 3, 4], [4, 3, 2])

# Initial cognitive distance
print("Initial cognitive distance:", cognitive_distance(agent1, agent2))

# Agents interact
agent1.interact(agent2)

# Cognitive distance after interaction
print("Cognitive distance after interaction:", cognitive_distance(agent1, agent2))

# Recursive interaction
for _ in range(5):
    agent1.interact(agent2)

# Cognitive distance after recursive interactions
print("Cognitive distance after recursive interactions:", cognitive_distance(agent1, agent2))
```

This code defines an `Agent` class with methods to update ideas and strategies, remember interactions, and interact with other agents. The cognitive distance is calculated as the sum of Euclidean distances between their ideas and strategies. The example shows how agents can interact and update their cognitive attributes, which are stored in a recursive memory of past interactions. This model can be expanded with more complex memory and interaction dynamics as needed.
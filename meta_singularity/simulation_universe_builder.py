Here's a Python code example that creates a simple logic universe to test strategies in artificial systems. This example will use a basic simulation environment where agents can make decisions based on simple rules. We'll use a grid world where agents can move and interact based on predefined strategies.

```python
import numpy as np
import random

class Environment:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = np.zeros((size, size))
        self.agents = [Agent(id=i, strategy=random.choice(['cooperate', 'defect'])) for i in range(num_agents)]
        self.place_agents()

    def place_agents(self):
        for agent in self.agents:
            while True:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
                if self.grid[x, y] == 0:
                    self.grid[x, y] = agent.id + 1
                    agent.position = (x, y)
                    break

    def move_agent(self, agent):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while directions:
            direction = random.choice(directions)
            new_x = agent.position[0] + direction[0]
            new_y = agent.position[1] + direction[1]
            if 0 <= new_x < self.size and 0 <= new_y < self.size and self.grid[new_x, new_y] == 0:
                self.grid[agent.position] = 0
                self.grid[new_x, new_y] = agent.id + 1
                agent.position = (new_x, new_y)
                break
            directions.remove(direction)

    def update(self):
        for agent in self.agents:
            self.move_agent(agent)

    def display(self):
        print(self.grid)

class Agent:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.position = None

    def decide(self, neighbors):
        if self.strategy == 'cooperate':
            return 'C'
        elif self.strategy == 'defect':
            return 'D'

def main():
    env = Environment(size=10, num_agents=5)
    steps = 10
    for _ in range(steps):
        env.update()
        env.display()
        print()

if __name__ == "__main__":
    main()
```

This code defines an environment where agents are placed randomly on a grid. Each agent can either cooperate or defect, and they move randomly around the grid. The environment updates by moving each agent, and the grid is displayed after each move. This setup can be expanded with more complex interaction rules and strategies to simulate different logic universes and test various strategies in artificial systems.
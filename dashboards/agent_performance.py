Below is a Python script that simulates a simple environment where agents can perform actions, survive based on their actions, and receive scores based on their effectiveness. This script includes a basic framework for agent behavior, survival checks, and reinforcement through a scoring system.

```python
import random

class Agent:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def act(self):
        # Randomly decide an action (0 = no action, 1 = good action, 2 = bad action)
        return random.choice([0, 1, 2])

    def update_health(self, action):
        if action == 1:
            self.health += 10  # Good action improves health
        elif action == 2:
            self.health -= 20  # Bad action reduces health
        self.health = min(100, max(0, self.health))  # Keep health within bounds

    def update_score(self, action):
        if action == 1:
            self.score += 5  # Good action increases score
        elif action == 2:
            self.score -= 5  # Bad action decreases score

    def is_alive(self):
        return self.health > 0

class Environment:
    def __init__(self, num_agents):
        self.agents = [Agent(f"Agent_{i}") for i in range(num_agents)]

    def simulate_round(self):
        for agent in self.agents:
            if agent.is_alive():
                action = agent.act()
                agent.update_health(action)
                agent.update_score(action)

    def run_simulation(self, num_rounds):
        for _ in range(num_rounds):
            self.simulate_round()
            self.display_scores()

    def display_scores(self):
        print("\nCurrent Scores:")
        for agent in self.agents:
            print(f"{agent.name}: Health = {agent.health}, Score = {agent.score}")

# Parameters
NUM_AGENTS = 5
NUM_ROUNDS = 10

# Run the simulation
env = Environment(NUM_AGENTS)
env.run_simulation(NUM_ROUNDS)
```

### Explanation:
- **Agent Class**: Represents each agent with attributes for health and score. Agents can perform actions that affect their health and score.
- **Environment Class**: Manages multiple agents and simulates their interactions over several rounds. Each round, agents act, update their health and score based on their actions, and check for survival.
- **Simulation**: The environment is initialized with a number of agents, and the simulation runs for a specified number of rounds. After each round, the current scores and health of all agents are displayed.

This script can be expanded with more complex agent behaviors, different types of actions, and a more detailed environment interaction.
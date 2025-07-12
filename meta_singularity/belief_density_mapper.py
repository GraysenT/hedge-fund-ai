Below is a Python code example that simulates mapping the concentration of beliefs across recursive agents. This example uses a simple model where agents update their beliefs based on the beliefs of other agents they interact with. The agents are recursive in the sense that they consider the beliefs of others, who in turn consider the beliefs of others, and so on.

```python
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, belief):
        self.belief = belief

    def update_belief(self, other_agents):
        # Simple averaging of beliefs
        total_belief = sum(agent.belief for agent in other_agents)
        self.belief = total_belief / len(other_agents)

def simulate_agents(num_agents, num_iterations):
    # Initialize agents with random beliefs
    agents = [Agent(np.random.rand()) for _ in range(num_agents)]

    # Record initial beliefs
    belief_history = [agent.belief for agent in agents]

    for _ in range(num_iterations):
        for i in range(num_agents):
            # Each agent updates its belief based on the beliefs of all other agents
            other_agents = agents[:i] + agents[i+1:]
            agents[i].update_belief(other_agents)

        # Record beliefs after each iteration
        belief_history.append([agent.belief for agent in agents])

    return belief_history

def plot_belief_history(belief_history, num_agents):
    belief_history = np.array(belief_history)
    plt.figure(figsize=(10, 6))
    for i in range(num_agents):
        plt.plot(belief_history[:, i], label=f'Agent {i+1}')
    plt.title('Belief Evolution Over Time')
    plt.xlabel('Iteration')
    plt.ylabel('Belief')
    plt.legend()
    plt.show()

# Parameters
num_agents = 5
num_iterations = 20

# Simulation
belief_history = simulate_agents(num_agents, num_iterations)

# Plotting
plot_belief_history(belief_history, num_agents)
```

This code defines a simple agent-based model where each agent starts with a random belief between 0 and 1. Agents update their beliefs by averaging the beliefs of all other agents, simulating a form of recursive belief updating. The simulation runs for a specified number of iterations, and the evolution of beliefs is plotted over time. This can be seen as a basic model of how consensus or divergence in beliefs might occur in a network of interacting recursive agents.
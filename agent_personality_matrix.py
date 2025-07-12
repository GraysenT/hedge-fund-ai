```python
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, name, risk, trust, ethics, ambition):
        self.name = name
        self.risk = risk
        self.trust = trust
        self.ethics = ethics
        self.ambition = ambition

    def __str__(self):
        return f"{self.name}: Risk={self.risk}, Trust={self.trust}, Ethics={self.ethics}, Ambition={self.ambition}"

def generate_agents(num_agents):
    names = [f"Agent_{i}" for i in range(num_agents)]
    agents = [Agent(name, np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()) for name in names]
    return agents

def plot_agents(agents):
    fig, ax = plt.subplots(2, 2, figsize=(10, 10))
    
    ax[0, 0].scatter([agent.risk for agent in agents], [agent.trust for agent in agents])
    ax[0, 0].set_xlabel('Risk')
    ax[0, 0].set_ylabel('Trust')
    ax[0, 0].set_title('Risk vs Trust')

    ax[0, 1].scatter([agent.ethics for agent in agents], [agent.ambition for agent in agents])
    ax[0, 1].set_xlabel('Ethics')
    ax[0, 1].set_ylabel('Ambition')
    ax[0, 1].set_title('Ethics vs Ambition')

    ax[1, 0].scatter([agent.risk for agent in agents], [agent.ethics for agent in agents])
    ax[1, 0].set_xlabel('Risk')
    ax[1, 0].set_ylabel('Ethics')
    ax[1, 0].set_title('Risk vs Ethics')

    ax[1, 1].scatter([agent.trust for agent in agents], [agent.ambition for agent in agents])
    ax[1, 1].set_xlabel('Trust')
    ax[1, 1].set_ylabel('Ambition')
    ax[1, 1].set_title('Trust vs Ambition')

    plt.tight_layout()
    plt.show()

def main():
    num_agents = 10
    agents = generate_agents(num_agents)
    for agent in agents:
        print(agent)
    plot_agents(agents)

if __name__ == "__main__":
    main()
```
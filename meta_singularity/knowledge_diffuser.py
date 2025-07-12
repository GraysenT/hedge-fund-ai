```python
import random

class Agent:
    def __init__(self, traits=None):
        if traits is None:
            traits = {}
        self.traits = traits

    def __str__(self):
        return f"Agent(traits={self.traits})"

def spread_traits(agents, spread_chance=0.1):
    """Spread traits among agents with a given chance."""
    if not agents:
        return

    # Collect all unique traits
    all_traits = {}
    for agent in agents:
        for trait, value in agent.traits.items():
            if trait not in all_traits or random.random() < 0.5:
                all_traits[trait] = value

    # Spread traits to other agents
    for agent in agents:
        for trait, value in all_traits.items():
            if trait not in agent.traits and random.random() < spread_chance:
                agent.traits[trait] = value

def main():
    # Create a population of agents with different traits
    population = [
        Agent({'intelligence': 'high', 'curiosity': 'medium'}),
        Agent({'strength': 'strong'}),
        Agent({'endurance': 'high'}),
        Agent({'intelligence': 'medium'}),
        Agent({'curiosity': 'high'}),
    ]

    print("Before spreading traits:")
    for agent in population:
        print(agent)

    # Spread traits among the agent population
    spread_traits(population, spread_chance=0.3)

    print("\nAfter spreading traits:")
    for agent in population:
        print(agent)

if __name__ == "__main__":
    main()
```
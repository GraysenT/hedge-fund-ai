```python
import random

class Agent:
    def __init__(self, attributes):
        self.attributes = attributes

    def __eq__(self, other):
        return self.attributes == other.attributes

    def __hash__(self):
        return hash(tuple(self.attributes))

def generate_random_attributes(num_attributes):
    return [random.randint(1, 100) for _ in range(num_attributes)]

def create_unique_agent(existing_agents, num_attributes):
    while True:
        new_attributes = generate_random_attributes(num_attributes)
        new_agent = Agent(new_attributes)
        if new_agent not in existing_agents:
            existing_agents.add(new_agent)
            return new_agent

def main():
    num_agents = 10
    num_attributes = 5
    existing_agents = set()

    for _ in range(num_agents):
        agent = create_unique_agent(existing_agents, num_attributes)
        print(f"Generated Agent with attributes: {agent.attributes}")

if __name__ == "__main__":
    main()
```
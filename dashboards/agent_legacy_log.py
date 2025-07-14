Below is a Python code example that implements a system to track the history of agents in terms of their status changes such as being retired, reborn, or evolved. This example uses a simple class structure to manage the agents and their histories.

```python
class Agent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = 'active'  # Possible statuses: active, retired, reborn, evolved
        self.history = []

    def retire(self):
        if self.status != 'retired':
            self.status = 'retired'
            self.history.append((self.status, 'Agent was retired.'))
            print(f"Agent {self.name} has been retired.")
        else:
            print(f"Agent {self.name} is already retired.")

    def reborn(self):
        if self.status != 'active':
            self.status = 'reborn'
            self.history.append((self.status, 'Agent was reborn.'))
            print(f"Agent {self.name} has been reborn.")
        else:
            print(f"Agent {self.name} is already active.")

    def evolve(self):
        if self.status != 'evolved':
            self.status = 'evolved'
            self.history.append((self.status, 'Agent has evolved.'))
            print(f"Agent {self.name} has evolved.")
        else:
            print(f"Agent {self.name} has already evolved.")

    def print_history(self):
        print(f"History of Agent {self.name}:")
        for status, description in self.history:
            print(f"Status: {status}, Description: {description}")

# Example usage
agent1 = Agent(1, "Agent One")
agent1.retire()
agent1.reborn()
agent1.evolve()
agent1.print_history()
```

This code defines an `Agent` class with methods to retire, reborn, and evolve an agent. Each action updates the agent's status and records the change in the agent's history. The `print_history` method can be used to display the history of status changes for an agent.
```python
class Agent:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules

class Module:
    def __init__(self, name, signals):
        self.name = name
        self.signals = signals

class Signal:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

# Define signals
signal1 = Signal("Signal1", "Module1")
signal2 = Signal("Signal2", "Module1")
signal3 = Signal("Signal3", "Module2")
signal4 = Signal("Signal4", "Module2")

# Define modules
module1 = Module("Module1", [signal1, signal2])
module2 = Module("Module2", [signal3, signal4])

# Define agents
agent1 = Agent("Agent1", [module1, module2])

# Function to print the master index
def print_master_index(agent):
    print(f"Agent Name: {agent.name}")
    for module in agent.modules:
        print(f"  Module Name: {module.name}")
        for signal in module.signals:
            print(f"    Signal Name: {signal.name}, Origin: {signal.origin}")

# Display the master index
print_master_index(agent1)
```
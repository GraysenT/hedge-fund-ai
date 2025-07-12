Below is a Python code that manages active generation IDs of strategies and tracks transitions between them. This code includes a class to handle the generation IDs and transitions, providing methods to activate, deactivate, and retrieve the current active generation.

```python
class StrategyGenerationManager:
    def __init__(self):
        self.active_generations = {}
        self.history = []

    def activate_generation(self, strategy_id, generation_id):
        """Activates a generation for a given strategy."""
        if strategy_id in self.active_generations:
            current_generation = self.active_generations[strategy_id]
            if current_generation != generation_id:
                self.history.append((strategy_id, current_generation, generation_id))
        self.active_generations[strategy_id] = generation_id
        print(f"Activated generation {generation_id} for strategy {strategy_id}")

    def deactivate_generation(self, strategy_id):
        """Deactivates the current generation for a given strategy."""
        if strategy_id in self.active_generations:
            deactivated_generation = self.active_generations.pop(strategy_id)
            print(f"Deactivated generation {deactivated_generation} for strategy {strategy_id}")
        else:
            print(f"No active generation found for strategy {strategy_id}")

    def get_current_generation(self, strategy_id):
        """Returns the current active generation for a given strategy."""
        return self.active_generations.get(strategy_id, None)

    def get_transition_history(self):
        """Returns the history of all generation transitions."""
        return self.history

# Example usage:
manager = StrategyGenerationManager()
manager.activate_generation("strategy1", 101)
manager.activate_generation("strategy2", 201)
manager.activate_generation("strategy1", 102)
print("Current generation for strategy1:", manager.get_current_generation("strategy1"))
manager.deactivate_generation("strategy2")
print("Transition history:", manager.get_transition_history())
```

This script defines a `StrategyGenerationManager` class that can activate, deactivate, and track generations for different strategies. It also maintains a history of all transitions between generations for each strategy. The example usage demonstrates activating generations for two strategies, updating a generation, and then deactivating a generation, followed by printing the current generation and the history of transitions.
```python
import json
import os

class StrategyConfigManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.configurations = self.load_configurations()

    def load_configurations(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_configurations(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.configurations, file, indent=4)

    def update_configuration(self, strategy_name, configuration):
        self.configurations[strategy_name] = configuration
        self.save_configurations()

    def revert_to_last_working(self, strategy_name):
        if strategy_name in self.configurations:
            return self.configurations[strategy_name]
        else:
            raise ValueError("No configuration found for the specified strategy.")

    def remove_configuration(self, strategy_name):
        if strategy_name in self.configurations:
            del self.configurations[strategy_name]
            self.save_configurations()
        else:
            raise ValueError("No configuration found to remove for the specified strategy.")

# Example usage
config_manager = StrategyConfigManager('configurations.json')

# Update a strategy configuration
config_manager.update_configuration('high_alpha_strategy_1', {'param1': 10, 'param2': 20})

# Revert to the last working configuration of a strategy
last_working_config = config_manager.revert_to_last_working('high_alpha_strategy_1')
print("Reverted to configuration:", last_working_config)

# Remove a strategy configuration
config_manager.remove_configuration('high_alpha_strategy_1')
```

This Python code defines a `StrategyConfigManager` class that manages configurations for different strategies, storing them in a JSON file. It allows updating, reverting, and removing configurations for specified strategies.
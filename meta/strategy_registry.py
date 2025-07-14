class ModuleRegistry:
    def __init__(self):
        self.modules = {}
        self.strategies = {}
        self.metadata = {}

    def register_module(self, module_name, module):
        self.modules[module_name] = module
        print(f"Module {module_name} registered.")

    def register_strategy(self, strategy_name, strategy):
        self.strategies[strategy_name] = strategy
        print(f"Strategy {strategy_name} registered.")

    def add_metadata(self, key, value):
        self.metadata[key] = value
        print(f"Metadata {key}: {value} added.")

    def get_module(self, module_name):
        return self.modules.get(module_name, None)

    def get_strategy(self, strategy_name):
        return self.strategies.get(strategy_name, None)

    def get_metadata(self, key):
        return self.metadata.get(key, None)

# Example usage
registry = ModuleRegistry()

# Registering modules
registry.register_module("auth", {"version": "1.0", "author": "John Doe"})
registry.register_module("payment", {"version": "2.0", "author": "Jane Smith"})

# Registering strategies
registry.register_strategy("login", lambda username, password: username == "admin" and password == "admin")
registry.register_strategy("pay", lambda amount: amount > 0)

# Adding metadata
registry.add_metadata("last_update", "2023-12-01")
registry.add_metadata("project", "Central Registry System")

# Accessing registered items
auth_module = registry.get_module("auth")
login_strategy = registry.get_strategy("login")
last_update = registry.get_metadata("last_update")

print(auth_module)
print(login_strategy(True, "admin", "admin"))
print(last_update)
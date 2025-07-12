Below is a Python implementation of a basic system to manage trust or influence between different modules in a software system. This example uses a simple class structure to represent modules and a manager class to handle the relationships and trust scores between them.

```python
class Module:
    def __init__(self, name):
        self.name = name
        self.trust_scores = {}

    def set_trust(self, other_module, score):
        self.trust_scores[other_module.name] = score

    def get_trust(self, other_module):
        return self.trust_scores.get(other_module.name, 0)

    def __str__(self):
        return f"Module({self.name})"


class TrustManager:
    def __init__(self):
        self.modules = {}

    def add_module(self, module):
        self.modules[module.name] = module

    def set_trust(self, module_from, module_to, score):
        if module_from in self.modules and module_to in self.modules:
            self.modules[module_from].set_trust(self.modules[module_to], score)

    def get_trust(self, module_from, module_to):
        if module_from in self.modules and module_to in self.modules:
            return self.modules[module_from].get_trust(self.modules[module_to])
        return 0

    def display_trust_network(self):
        for name, module in self.modules.items():
            print(f"Trust relationships for {name}:")
            for target, score in module.trust_scores.items():
                print(f"  {name} -> {target} : {score}")


# Example usage
if __name__ == "__main__":
    # Create modules
    module_a = Module("ModuleA")
    module_b = Module("ModuleB")
    module_c = Module("ModuleC")

    # Create TrustManager and add modules
    manager = TrustManager()
    manager.add_module(module_a)
    manager.add_module(module_b)
    manager.add_module(module_c)

    # Set trust scores
    manager.set_trust("ModuleA", "ModuleB", 75)
    manager.set_trust("ModuleB", "ModuleC", 85)
    manager.set_trust("ModuleC", "ModuleA", 50)
    manager.set_trust("ModuleA", "ModuleC", 60)

    # Display all trust relationships
    manager.display_trust_network()
```

This code defines two classes, `Module` and `TrustManager`. Each `Module` can have trust scores associated with other modules. The `TrustManager` handles adding modules and managing the trust relationships between them. It also provides a method to display all trust relationships in the system.

The example usage at the bottom demonstrates how to create modules, set trust scores between them, and print out the trust network. This could be expanded with more complex trust calculation mechanisms, depending on the specific requirements of your application.
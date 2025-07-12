```python
import copy

class ModuleRegistry:
    def __init__(self):
        self.modules = {}
        self.backup = {}

    def add_module(self, module_name, module):
        self.modules[module_name] = module
        self.backup[module_name] = copy.deepcopy(module)

    def get_module(self, module_name):
        return self.modules.get(module_name)

    def update_module(self, module_name, new_module):
        if module_name in self.modules:
            self.modules[module_name] = new_module

    def restore_module(self, module_name):
        if module_name in self.backup:
            self.modules[module_name] = copy.deepcopy(self.backup[module_name])

    def delete_module(self, module_name):
        if module_name in self.modules:
            del self.modules[module_name]
            del self.backup[module_name]

# Example usage
registry = ModuleRegistry()
registry.add_module("math_module", {"add": lambda x, y: x + y})
print("Original:", registry.get_module("math_module")["add"](1, 2))

# Simulate module mutation
registry.update_module("math_module", {"add": lambda x, y: x * y})
print("Mutated:", registry.get_module("math_module")["add"](1, 2))

# Restore original module
registry.restore_module("math_module")
print("Restored:", registry.get_module("math_module")["add"](1, 2))
```
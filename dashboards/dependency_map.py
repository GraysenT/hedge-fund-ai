Below is a Python script that simulates a simple module dependency system and demonstrates how updates to one module can propagate to others that depend on it. This example uses a directed graph to represent dependencies, where an edge from module A to module B means that module A depends on module B.

```python
from collections import defaultdict, deque

class ModuleDependencyGraph:
    def __init__(self):
        # Using defaultdict to automatically handle missing keys
        self.dependencies = defaultdict(set)
        self.dependents = defaultdict(set)

    def add_dependency(self, module, depends_on):
        """ Add a dependency where 'module' depends on 'depends_on' """
        self.dependencies[module].add(depends_on)
        self.dependents[depends_on].add(module)

    def remove_dependency(self, module, depends_on):
        """ Remove a dependency """
        if depends_on in self.dependencies[module]:
            self.dependencies[module].remove(depends_on)
            self.dependents[depends_on].remove(module)

    def update_module(self, module):
        """ Simulate an update to a module and propagate it to dependent modules """
        # Use a queue to handle updates in breadth-first manner
        queue = deque([module])
        updated_modules = set()

        while queue:
            current_module = queue.popleft()
            if current_module not in updated_modules:
                print(f"Updating {current_module}")
                updated_modules.add(current_module)
                # Enqueue all modules that depend on the current module
                for dependent in self.dependents[current_module]:
                    queue.append(dependent)

def main():
    graph = ModuleDependencyGraph()
    # Adding some dependencies
    graph.add_dependency('ModuleA', 'ModuleB')  # A depends on B
    graph.add_dependency('ModuleC', 'ModuleA')  # C depends on A
    graph.add_dependency('ModuleC', 'ModuleB')  # C also depends on B
    graph.add_dependency('ModuleD', 'ModuleC')  # D depends on C

    # Simulate updating ModuleB
    print("Starting updates from ModuleB:")
    graph.update_module('ModuleB')

if __name__ == "__main__":
    main()
```

This script defines a `ModuleDependencyGraph` class that can add and remove dependencies between modules and propagate updates using a breadth-first search approach. When a module is updated, all modules that directly or indirectly depend on it are also marked for updates in sequence. This example can be expanded with more complex dependency scenarios and additional features like version handling, cyclic dependency checks, and more.
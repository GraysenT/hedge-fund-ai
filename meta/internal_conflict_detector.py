```python
class Module:
    def __init__(self, name, description, principles):
        self.name = name
        self.description = description
        self.principles = principles

    def __str__(self):
        return f"Module: {self.name}\nDescription: {self.description}\nPrinciples: {self.principles}\n"

def check_for_contradictions(modules):
    contradictions = []
    num_modules = len(modules)

    for i in range(num_modules):
        for j in range(i + 1, num_modules):
            shared_principles = set(modules[i].principles) & set(modules[j].principles)
            if shared_principles:
                for principle in shared_principles:
                    if ("not " + principle in modules[i].principles or
                        "not " + principle in modules[j].principles):
                        contradictions.append((modules[i].name, modules[j].name, principle))
    return contradictions

# Example usage
module1 = Module("Module1", "Handles user data", ["privacy", "security", "not transparency"])
module2 = Module("Module2", "Handles financial transactions", ["transparency", "security"])
module3 = Module("Module3", "Marketing", ["privacy", "transparency"])

modules = [module1, module2, module3]

contradictions = check_for_contradictions(modules)
for mod1, mod2, principle in contradictions:
    print(f"Contradiction found between {mod1} and {mod2} on principle: {principle}")
```

This Python code defines a system to detect contradictions between different modules based on their principles. Each module has a set of principles, and the code checks for direct contradictions where one module explicitly states a principle and another states the opposite.
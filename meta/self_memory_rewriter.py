```python
class PerspectiveMemory:
    def __init__(self):
        self.memory = {}

    def update_memory(self, key, value):
        self.memory[key] = value

    def get_memory(self, key):
        return self.memory.get(key, "No record found.")

    def shift_perspective(self, key, new_value):
        if key in self.memory:
            old_value = self.memory[key]
            if old_value != new_value:
                self.memory[key] = new_value
                print(f"Memory updated for {key}: from {old_value} to {new_value}")
            else:
                print(f"No change required for {key}.")
        else:
            self.memory[key] = new_value
            print(f"New memory added for {key} with value {new_value}")

# Example usage
memory_system = PerspectiveMemory()
memory_system.update_memory("priority", "high")
print(memory_system.get_memory("priority"))
memory_system.shift_perspective("priority", "medium")
print(memory_system.get_memory("priority"))
memory_system.shift_perspective("truth", "variable")
print(memory_system.get_memory("truth"))
```
This Python code defines a class `PerspectiveMemory` that manages an internal memory dictionary. It allows updating, retrieving, and shifting perspectives (values) based on changes in priority or truth.
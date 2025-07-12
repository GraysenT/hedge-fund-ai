Below is a Python example that simulates routing memory writes and loads to long-term and fast-access pools. This example uses dictionaries to represent the memory pools, where the `long_term_memory` is used for less frequently accessed data and `fast_access_memory` for data that is accessed more often. The code includes basic management for moving data between these pools based on access frequency.

```python
class MemoryManager:
    def __init__(self, fast_access_capacity=5):
        self.long_term_memory = {}
        self.fast_access_memory = {}
        self.fast_access_capacity = fast_access_capacity
        self.access_counter = {}

    def write(self, key, value):
        # Write directly to long-term memory
        self.long_term_memory[key] = value
        # Initialize access counter for this key
        self.access_counter[key] = 0

    def load(self, key):
        # Check if the key is in fast access memory first
        if key in self.fast_access_memory:
            self.access_counter[key] += 1
            return self.fast_access_memory[key]
        elif key in self.long_term_memory:
            # Move to fast access memory if accessed frequently
            self.access_counter[key] += 1
            if self.access_counter[key] >= 3:  # Threshold for frequent access
                self._move_to_fast_access(key)
            return self.long_term_memory[key]
        else:
            raise KeyError(f"Key {key} not found in memory.")

    def _move_to_fast_access(self, key):
        if len(self.fast_access_memory) >= self.fast_access_capacity:
            # Find least frequently accessed item in fast access memory to move back to long-term
            least_accessed_key = min(self.fast_access_memory, key=lambda k: self.access_counter[k])
            self._move_to_long_term(least_accessed_key)
        
        # Move the frequently accessed item to fast access memory
        self.fast_access_memory[key] = self.long_term_memory.pop(key)

    def _move_to_long_term(self, key):
        # Move an item back to long-term memory
        self.long_term_memory[key] = self.fast_access_memory.pop(key)

    def display_memories(self):
        print("Long-Term Memory:", self.long_term_memory)
        print("Fast-Access Memory:", self.fast_access_memory)
        print("Access Counter:", self.access_counter)

# Example usage
memory_manager = MemoryManager()

# Simulating writes
memory_manager.write("a", 100)
memory_manager.write("b", 200)
memory_manager.write("c", 300)
memory_manager.write("d", 400)
memory_manager.write("e", 500)

# Simulating loads
print(memory_manager.load("a"))  # First access
print(memory_manager.load("a"))  # Second access
print(memory_manager.load("a"))  # Third access, should move to fast access
print(memory_manager.load("b"))
print(memory_manager.load("c"))
print(memory_manager.load("d"))
print(memory_manager.load("e"))

# Display current state of memories
memory_manager.display_memories()
```

This code defines a `MemoryManager` class that manages two types of memory pools and moves data between them based on access frequency. The `write` method writes data to long-term memory, and the `load` method checks if data should be moved to fast-access memory after being accessed frequently. The example demonstrates basic operations and shows how data is moved between the pools. Adjust the `fast_access_capacity` and access frequency threshold as needed for different scenarios.
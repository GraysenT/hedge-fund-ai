```python
import time

class SystemValueTracker:
    def __init__(self):
        self.start_time = time.time()
        self.logic_value = 0
        self.purpose_value = 0

    def update_logic_value(self, increment):
        self.logic_value += increment
        print(f"Updated logic value: {self.logic_value}")

    def update_purpose_value(self, increment):
        self.purpose_value += increment
        print(f"Updated purpose value: {self.purpose_value}")

    def get_system_age(self):
        return time.time() - self.start_time

    def report(self):
        age = self.get_system_age()
        print(f"System age: {age} seconds")
        print(f"Current logic value: {self.logic_value}")
        print(f"Current purpose value: {self.purpose_value}")

# Example usage
tracker = SystemValueTracker()
tracker.update_logic_value(10)
tracker.update_purpose_value(20)
time.sleep(2)  # Simulate time passing
tracker.report()
```
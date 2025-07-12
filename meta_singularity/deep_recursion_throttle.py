```python
import sys
import threading
import time
import random

class SystemStrainMonitor:
    def __init__(self):
        self.high_strain = False
        self.lock = threading.Lock()

    def simulate_strain(self):
        # Simulate system strain randomly
        while True:
            with self.lock:
                self.high_strain = random.choice([True, False])
            time.sleep(1)

    def is_high_strain(self):
        with self.lock:
            return self.high_strain

def recursive_function(count, max_depth, monitor):
    if count >= max_depth:
        return count
    if monitor.is_high_strain():
        print(f"System under strain. Current recursion depth: {count}")
        time.sleep(1)  # Simulate reduced processing due to strain
    return recursive_function(count + 1, max_depth, monitor)

def main():
    monitor = SystemStrainMonitor()
    threading.Thread(target=monitor.simulate_strain, daemon=True).start()

    max_depth = 100
    sys.setrecursionlimit(max_depth + 10)  # Set a safe recursion limit

    result = recursive_function(0, max_depth, monitor)
    print(f"Reached recursion depth: {result}")

if __name__ == "__main__":
    main()
```
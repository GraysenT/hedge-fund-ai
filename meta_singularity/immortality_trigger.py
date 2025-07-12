```python
import threading

class SystemState:
    def __init__(self):
        self.lock = threading.Lock()
        self.system_stable = True

    def check_system_state(self):
        # Simulate checking the system's state
        # This could be replaced with actual checks in a real system
        import random
        return random.choice([True, False])

    def halt_evolution(self):
        print("System is halting to prevent collapse.")
        # Add actual code to halt system processes

    def monitor_system(self):
        while True:
            with self.lock:
                if not self.check_system_state():
                    self.system_stable = False
                    self.halt_evolution()
                    break
            # Sleep to simulate time delay between checks
            import time
            time.sleep(1)

# Example usage
system_state = SystemState()
monitor_thread = threading.Thread(target=system_state.monitor_system)
monitor_thread.start()
```
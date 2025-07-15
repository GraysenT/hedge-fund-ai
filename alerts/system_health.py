Below is a Python script that simulates monitoring the health status and error signals across multiple modules in a system. This example uses threading to simulate real-time monitoring and logging to handle the outputs. Each module will have a random chance of encountering an error, and the health status will be reported periodically.

```python
import threading
import time
import random
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for simulation
NUMBER_OF_MODULES = 5
HEALTH_CHECK_INTERVAL = 5  # seconds
SIMULATION_DURATION = 30  # seconds

class Module:
    def __init__(self, module_id):
        self.module_id = module_id
        self.is_healthy = True

    def check_health(self):
        # Simulate health check with a random failure
        if random.random() < 0.1:  # 10% chance of failure
            self.is_healthy = False
            logging.error(f"Module {self.module_id} has failed.")
        else:
            self.is_healthy = True
            logging.info(f"Module {self.module_id} is healthy.")

def monitor_module(module):
    while True:
        module.check_health()
        time.sleep(HEALTH_CHECK_INTERVAL)

def main():
    modules = [Module(i) for i in range(NUMBER_OF_MODULES)]
    threads = []

    # Create and start threads for each module
    for module in modules:
        thread = threading.Thread(target=monitor_module, args=(module,))
        thread.start()
        threads.append(thread)

    # Run the simulation for a fixed duration
    time.sleep(SIMULATION_DURATION)

    # Stop all threads after the simulation
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
```

### Explanation:
- **Module Class**: Represents a module with an ID and a health status. It has a method `check_health` that randomly determines if the module is healthy or not.
- **monitor_module Function**: Continuously checks the health of a given module at fixed intervals.
- **main Function**: Sets up the modules and threads, runs them for a specified duration, and then stops them.

This script will log the health status of each module every few seconds and report any errors encountered. Adjust the `NUMBER_OF_MODULES`, `HEALTH_CHECK_INTERVAL`, and `SIMULATION_DURATION` constants as needed for different scenarios.
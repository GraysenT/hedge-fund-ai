Here's a Python script that monitors and displays system loop timing and performance by module and action. This script uses the `time` module to measure execution time and organizes the performance data by module and action.

```python
import time
import random

# Simulated modules and actions
modules = {
    'network': ['fetch_data', 'send_data'],
    'database': ['query', 'update'],
    'processing': ['compute', 'transform']
}

# Function to simulate action execution time
def simulate_action(module, action):
    print(f"Executing {action} in {module}...")
    execution_time = random.uniform(0.1, 1.0)  # Simulate time between 0.1 and 1.0 seconds
    time.sleep(execution_time)
    return execution_time

# Main function to monitor performance
def monitor_performance(modules):
    performance_data = {}
    
    for module, actions in modules.items():
        module_data = {}
        for action in actions:
            start_time = time.time()
            execution_time = simulate_action(module, action)
            end_time = time.time()
            module_data[action] = {
                'start_time': start_time,
                'end_time': end_time,
                'execution_time': execution_time
            }
        performance_data[module] = module_data
    
    return performance_data

# Function to display performance data
def display_performance(performance_data):
    for module, actions in performance_data.items():
        print(f"\nModule: {module}")
        for action, timings in actions.items():
            print(f"  Action: {action}")
            print(f"    Start Time: {timings['start_time']:.2f}")
            print(f"    End Time: {timings['end_time']:.2f}")
            print(f"    Execution Time: {timings['execution_time']:.2f} seconds")

# Run the monitoring and display the results
performance_data = monitor_performance(modules)
display_performance(performance_data)
```

### Explanation:
1. **Modules and Actions**: The script defines a dictionary `modules` that contains different modules and their respective actions.

2. **Simulate Action**: The `simulate_action` function simulates the execution of an action within a module by sleeping for a random amount of time between 0.1 and 1.0 seconds.

3. **Monitor Performance**: The `monitor_performance` function iterates over each module and its actions, measures the execution time, and stores the performance data.

4. **Display Performance**: The `display_performance` function prints out the performance data for each module and action, including start time, end time, and execution time.

This script can be extended or modified to include real actions and modules, integrate with actual logging systems, or handle more complex performance metrics.
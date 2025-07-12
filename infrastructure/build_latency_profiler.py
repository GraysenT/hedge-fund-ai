Below is an example Python script that profiles the build and update latency of each module in a hypothetical software system. This script uses Python's `time` module to measure execution time and simulates different modules with varying complexities. The script also includes a simple mechanism to update the modules and measure the update latency.

```python
import time

# Simulating different modules in a software system
def module_a():
    time.sleep(0.2)  # Simulate some processing time

def module_b():
    time.sleep(0.5)  # Simulate more processing time

def module_c():
    time.sleep(0.1)  # Simulate less processing time

# Function to build all modules
def build_modules():
    start_time = time.time()
    module_a()
    module_b()
    module_c()
    end_time = time.time()
    print(f"Total build time: {end_time - start_time:.2f} seconds")

# Function to update each module and measure latency
def update_module(module, module_name):
    start_time = time.time()
    module()
    end_time = time.time()
    print(f"Update time for {module_name}: {end_time - start_time:.2f} seconds")

# Main function to profile build and update latencies
def main():
    print("Building all modules...")
    build_modules()
    
    print("\nUpdating individual modules...")
    update_module(module_a, "Module A")
    update_module(module_b, "Module B")
    update_module(module_c, "Module C")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Modules Simulation**: `module_a`, `module_b`, and `module_c` are functions simulating different modules with varying execution times using `time.sleep()`.

2. **Build Function**: `build_modules()` builds all the modules sequentially and calculates the total build time.

3. **Update Function**: `update_module()` updates a specific module and measures the time taken to update that module. It is called for each module to profile individual update latencies.

4. **Main Function**: `main()` orchestrates the building and updating of modules, providing a clear output of the time taken for each operation.

This script can be adapted to real modules by replacing the simulated functions with actual module initialization and update calls.
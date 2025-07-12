Below is a Python script that uses the `sys` and `importlib` modules to estimate the memory usage of each imported module. It also calculates memory efficiency based on the number of functions and classes defined in the module. This script uses the `pympler` library to get more accurate memory usage information, so you will need to install it first using `pip install pympler`.

```python
import sys
import importlib
from pympler import asizeof

def get_module_size(module):
    """Estimate memory footprint of the given module."""
    return asizeof.asizeof(module)

def get_module_efficiency(module):
    """Calculate the memory efficiency based on the number of functions and classes."""
    num_items = len([item for item in dir(module) if callable(getattr(module, item))])
    if num_items == 0:
        return float('inf')  # Avoid division by zero; more items is more efficient
    module_size = get_module_size(module)
    return module_size / num_items

def list_modules_memory():
    """List memory usage and efficiency of all imported modules."""
    loaded_modules = sys.modules
    module_memory_usage = {}
    module_efficiency = {}

    for name, module in loaded_modules.items():
        if module is not None:
            try:
                memory_usage = get_module_size(module)
                efficiency = get_module_efficiency(module)
                module_memory_usage[name] = memory_usage
                module_efficiency[name] = efficiency
            except Exception as e:
                print(f"Error processing module {name}: {e}")

    # Sort modules by memory usage
    sorted_memory_usage = sorted(module_memory_usage.items(), key=lambda x: x[1], reverse=True)

    print("Memory usage by module:")
    for name, size in sorted_memory_usage:
        print(f"{name}: {size} bytes")

    print("\nMemory efficiency (bytes per function/class):")
    sorted_efficiency = sorted(module_efficiency.items(), key=lambda x: x[1])
    for name, eff in sorted_efficiency:
        print(f"{name}: {eff:.2f} bytes/item")

if __name__ == "__main__":
    list_modules_memory()
```

This script will print out the memory usage and memory efficiency of each module currently loaded in the Python environment. The efficiency is calculated as the total memory usage of the module divided by the number of callable items (functions and classes) it defines. Lower values indicate more memory efficiency per callable item.

Before running the script, ensure you have `pympler` installed:

```bash
pip install pympler
```

This script can be useful for understanding which modules are consuming the most memory and how efficiently they use that memory relative to the functionality they provide.
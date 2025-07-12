Below is a Python script that tracks fading modules and their expected shutdown timelines. The script uses a dictionary to store module names, their current status, and their expected shutdown dates. It provides functionality to add, update, and display modules and their shutdown timelines.

```python
from datetime import datetime, timedelta

class ModuleTracker:
    def __init__(self):
        self.modules = {}

    def add_module(self, module_name, status, shutdown_in_days):
        shutdown_date = datetime.now() + timedelta(days=shutdown_in_days)
        self.modules[module_name] = {'status': status, 'shutdown_date': shutdown_date}
        print(f"Module '{module_name}' added with shutdown date {shutdown_date.strftime('%Y-%m-%d')}.")

    def update_module(self, module_name, status=None, shutdown_in_days=None):
        if module_name in self.modules:
            if status:
                self.modules[module_name]['status'] = status
            if shutdown_in_days is not None:
                self.modules[module_name]['shutdown_date'] = datetime.now() + timedelta(days=shutdown_in_days)
            print(f"Module '{module_name}' updated.")
        else:
            print(f"Module '{module_name}' not found.")

    def display_modules(self):
        print("Current Modules and Shutdown Timelines:")
        for module, details in self.modules.items():
            print(f"Module: {module}, Status: {details['status']}, Shutdown Date: {details['shutdown_date'].strftime('%Y-%m-%d')}")

# Example usage
if __name__ == "__main__":
    tracker = ModuleTracker()
    tracker.add_module("Module1", "Active", 30)
    tracker.add_module("Module2", "Fading", 45)
    tracker.update_module("Module1", status="Critical", shutdown_in_days=15)
    tracker.display_modules()
```

This script defines a `ModuleTracker` class that can manage modules with their status and shutdown dates. It provides methods to add a new module, update an existing module, and display all modules with their details. The example usage at the end demonstrates how to use this class to manage module data.
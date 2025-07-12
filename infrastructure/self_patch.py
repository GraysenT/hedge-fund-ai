Below is a Python script that demonstrates how to apply hot patches to running modules when bugs or security risks are detected. This script uses the `importlib` module for reloading the updated module and `watchdog` to monitor file changes in real-time.

First, ensure you have the `watchdog` library installed. You can install it using pip:

```bash
pip install watchdog
```

Here's the Python script:

```python
import importlib
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the module you want to watch and patch
MODULE_TO_WATCH = 'module_to_patch'

# Import the module initially
try:
    module_to_patch = importlib.import_module(MODULE_TO_WATCH)
except ImportError:
    print(f"Failed to import module {MODULE_TO_WATCH}")
    sys.exit(1)

class PatchHandler(FileSystemEventHandler):
    """ Handler for file system events that applies a hot patch. """
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Detected changes in {event.src_path}. Applying hot patch...")
            self.apply_hot_patch()

    def apply_hot_patch(self):
        """ Reload the module to apply the patch. """
        try:
            # Reload the module
            importlib.reload(module_to_patch)
            print(f"Successfully reloaded module {MODULE_TO_WATCH}")
        except Exception as e:
            print(f"Failed to reload module {MODULE_TO_WATCH}: {e}")

def start_monitoring(path='.'):
    """ Start monitoring the module directory for any changes. """
    event_handler = PatchHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f"Monitoring changes in directory {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    # Path to the directory containing the module to watch
    module_path = '/path/to/your/module/directory'
    start_monitoring(module_path)
```

### How It Works:
1. **Module Importing**: The script starts by trying to import the module you want to watch. If the module doesn't exist, it exits.
2. **Event Handling**: It uses `watchdog` to create an event handler that listens for modifications to Python files.
3. **Hot Patching**: When a modification is detected, the script reloads the module using `importlib.reload()`. This is the "hot patch" as it updates the running module's code without restarting the application.
4. **Monitoring**: The script monitors the directory containing the module for changes and applies the hot patch whenever a change is detected.

### Note:
- Replace `'module_to_patch'` with the actual name of the module you want to patch.
- Update `'/path/to/your/module/directory'` to the path where your module files are located.
- This script assumes that the module files end with `.py` and are directly in the specified directory (not in subdirectories).

This script is a basic example and might need adjustments based on the specific requirements and environment in which it's used.
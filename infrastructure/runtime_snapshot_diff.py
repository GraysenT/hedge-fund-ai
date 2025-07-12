Below is a Python script that compares two system snapshots to identify changes between builds. It assumes that the snapshots are stored as JSON files, which might contain details like installed packages, system files, and configuration settings. The script will compare these two JSON files and output the differences.

```python
import json

def load_snapshot(file_path):
    """ Load the snapshot from a JSON file. """
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_snapshots(snapshot1, snapshot2):
    """ Compare two snapshots and return the differences. """
    changes = {
        'added': {},
        'removed': {},
        'changed': {}
    }

    # Check for additions and changes
    for key, value in snapshot2.items():
        if key not in snapshot1:
            changes['added'][key] = value
        elif snapshot1[key] != value:
            changes['changed'][key] = {'from': snapshot1[key], 'to': value}

    # Check for removals
    for key in snapshot1:
        if key not in snapshot2:
            changes['removed'][key] = snapshot1[key]

    return changes

def print_changes(changes):
    """ Print the changes in a readable format. """
    if changes['added']:
        print("Added:")
        for key, value in changes['added'].items():
            print(f"  {key}: {value}")
        print()

    if changes['removed']:
        print("Removed:")
        for key, value in changes['removed'].items():
            print(f"  {key}: {value}")
        print()

    if changes['changed']:
        print("Changed:")
        for key, value in changes['changed'].items():
            print(f"  {key}: from {value['from']} to {value['to']}")
        print()

def main():
    # Paths to the snapshot files
    snapshot1_path = 'snapshot1.json'
    snapshot2_path = 'snapshot2.json'

    # Load the snapshots
    snapshot1 = load_snapshot(snapshot1_path)
    snapshot2 = load_snapshot(snapshot2_path)

    # Compare the snapshots
    changes = compare_snapshots(snapshot1, snapshot2)

    # Print the changes
    print_changes(changes)

if __name__ == "__main__":
    main()
```

### How to Use This Script
1. Ensure you have two JSON files representing the snapshots of the system states at different times or builds. These files should be named `snapshot1.json` and `snapshot2.json`.
2. Place these files in the same directory as the script or modify the `snapshot1_path` and `snapshot2_path` variables in the `main()` function to point to the correct file locations.
3. Run the script. It will output the differences between the two snapshots, categorizing them into added, removed, and changed items.

### Note
This script assumes that the snapshots are in a dictionary format where each key-value pair represents a system attribute and its state. Depending on the complexity and structure of your system snapshots, you might need to adapt the comparison logic to handle nested dictionaries, lists, or other data types more appropriately.
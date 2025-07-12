Here's a Python script that simulates a system where you can rollback or restore any version of a system using evolution logs. This script uses a simple dictionary to store system states and allows the user to revert to any previous state using a version number.

```python
class SystemVersionControl:
    def __init__(self):
        self.versions = {}
        self.current_version = 0
        self.save_version(self.current_version, {})  # Initial empty state

    def save_version(self, version, state):
        self.versions[version] = state.copy()

    def update_system(self, changes):
        self.current_version += 1
        new_state = self.versions[self.current_version - 1].copy()
        new_state.update(changes)
        self.save_version(self.current_version, new_state)
        return self.current_version

    def rollback(self, version):
        if version in self.versions:
            self.current_version = version
            return self.versions[version]
        else:
            raise ValueError("Version does not exist")

    def get_current_state(self):
        return self.versions[self.current_version]

    def list_versions(self):
        return list(self.versions.keys())

# Example usage
if __name__ == "__main__":
    svc = SystemVersionControl()

    # Simulate system updates
    svc.update_system({'file1': 'content1'})
    svc.update_system({'file2': 'content2'})
    svc.update_system({'file1': 'new_content1', 'file3': 'content3'})

    # Print current system state
    print("Current State:", svc.get_current_state())

    # Rollback to version 1
    print("Rolling back to version 1...")
    state_v1 = svc.rollback(1)
    print("State at version 1:", state_v1)

    # List all versions
    print("All versions:", svc.list_versions())
```

This script defines a `SystemVersionControl` class that manages system states. Each state is stored in a dictionary, and changes to the system are recorded as new versions. Users can update the system, rollback to any previous version, and view the current system state or list all versions.
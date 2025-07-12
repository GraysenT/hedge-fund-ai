Below is a Python script that simulates the process of rebuilding a system architecture from compressed logic and memory backups. This script includes functionalities to decompress backup files, restore system configurations, and simulate the reinstallation of system components. It uses the `tarfile` module for handling compressed files and `json` for configuration management.

```python
import tarfile
import os
import json

def decompress_backup(backup_path, extract_to):
    """
    Decompresses a tar.gz backup file to a specified directory.
    """
    try:
        with tarfile.open(backup_path, "r:gz") as tar:
            tar.extractall(path=extract_to)
            print(f"Backup decompressed successfully to {extract_to}")
    except Exception as e:
        print(f"Error decompressing the backup: {e}")

def load_configuration(config_path):
    """
    Loads system configuration from a JSON file.
    """
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            print("Configuration loaded successfully.")
            return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None

def restore_system(config):
    """
    Simulates the restoration of system components based on the configuration.
    """
    if config is None:
        print("Invalid configuration. Cannot restore system.")
        return

    print("Restoring system components...")
    for component, settings in config.items():
        print(f"Restoring {component} with settings: {settings}")
    print("System restoration complete.")

def main():
    backup_path = 'path_to_backup.tar.gz'  # Path to the compressed backup file
    extract_to = 'restore_directory'  # Directory where the backup will be extracted
    config_path = os.path.join(extract_to, 'system_config.json')  # Path to the configuration file within the extracted backup

    # Step 1: Decompress the backup
    decompress_backup(backup_path, extract_to)

    # Step 2: Load system configuration
    config = load_configuration(config_path)

    # Step 3: Restore the system using the loaded configuration
    restore_system(config)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Decompress Backup**: The `decompress_backup` function takes a path to a compressed `.tar.gz` file and an extraction directory, then decompresses the file into that directory.
2. **Load Configuration**: The `load_configuration` function reads a JSON configuration file which defines how the system should be restored.
3. **Restore System**: The `restore_system` function simulates the process of restoring system components based on the configuration data.
4. **Main Function**: Orchestrates the process by calling the above functions in sequence.

### Usage:
To use this script, you need to specify the correct paths for `backup_path` and `extract_to`. Ensure the backup file contains a `system_config.json` file with the necessary configuration data.
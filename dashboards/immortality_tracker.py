Below is a Python script that monitors system self-repair, backup status, and seed regeneration logic. The script uses simulated functions to represent these processes. In a real-world scenario, you would replace these simulated functions with actual system calls or API requests.

```python
import time
import random
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_system_self_repair():
    """Simulate checking the system's self-repair status."""
    # Simulated status, in a real scenario this would be a system call or API request
    return random.choice(['healthy', 'repairing', 'failed'])

def check_backup_status():
    """Simulate checking the backup status."""
    # Simulated status
    return random.choice(['completed', 'in_progress', 'failed'])

def check_seed_regeneration():
    """Simulate checking seed regeneration logic."""
    # Simulated status
    return random.choice(['successful', 'regenerating', 'error'])

def monitor_system():
    while True:
        # Check system self-repair status
        repair_status = check_system_self_repair()
        logging.info(f"System self-repair status: {repair_status}")

        # Check backup status
        backup_status = check_backup_status()
        logging.info(f"Backup status: {backup_status}")

        # Check seed regeneration status
        seed_status = check_seed_regeneration()
        logging.info(f"Seed regeneration status: {seed_status}")

        # Sleep for some time before checking again
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    monitor_system()
```

### Explanation:
1. **Logging Setup**: The script uses Python's `logging` module to log information, which is more robust and flexible than simple print statements.

2. **Simulated Functions**: `check_system_self_repair`, `check_backup_status`, and `check_seed_regeneration` are placeholder functions that randomly return a status. In a real application, these would interface with actual system or network APIs to retrieve real statuses.

3. **Monitoring Loop**: The `monitor_system` function runs an infinite loop, repeatedly checking the statuses of system self-repair, backup, and seed regeneration every 10 seconds. It logs the status each time.

4. **Main Execution**: The script runs the `monitor_system` function if it is the main module executed, ensuring that it continuously monitors and logs the system statuses.

This script provides a basic framework for a monitoring system and can be expanded with real data sources, error handling, and more sophisticated logging and notification mechanisms (like sending emails or SMS alerts when certain conditions are met).
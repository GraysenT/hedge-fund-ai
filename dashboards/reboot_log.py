Below is a Python script that logs all partial or full system reboots, triggers, and outcome snapshots. This script uses the `logging` module to handle logging and `subprocess` to execute system commands that simulate checking for system reboots and triggers. It assumes a Linux environment where system logs can be checked using commands like `last reboot` for reboots and custom triggers can be defined and checked.

```python
import logging
import subprocess
import datetime

# Configure logging
logging.basicConfig(filename='system_reboot_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_reboots():
    """Check for system reboots and log them."""
    try:
        result = subprocess.run(['last', 'reboot'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Checked for reboots successfully.")
            return result.stdout
        else:
            logging.error("Failed to check for reboots: " + result.stderr)
    except Exception as e:
        logging.error("Error checking for reboots: " + str(e))

def check_custom_triggers():
    """Check for custom triggers (this function needs to be customized based on what triggers are relevant)."""
    # Example: Check if a specific file exists which might trigger a system action
    try:
        # This is just a placeholder for whatever trigger you need to check
        trigger_file = '/path/to/trigger/file'
        result = subprocess.run(['test', '-f', trigger_file], capture_output=True)
        if result.returncode == 0:
            logging.info("Trigger file exists.")
            return True
        else:
            logging.info("No trigger file found.")
            return False
    except Exception as e:
        logging.error("Error checking for custom triggers: " + str(e))
        return False

def log_snapshot():
    """Take a snapshot of the current system state."""
    try:
        # Example: Capture the current process list
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Snapshot of current processes taken.")
            return result.stdout
        else:
            logging.error("Failed to take snapshot of current processes: " + result.stderr)
    except Exception as e:
        logging.error("Error taking snapshot of system state: " + str(e))

def main():
    logging.info("System check started.")
    reboots = check_reboobs()
    if reboots:
        logging.info("Recent reboots:\n" + reboots)
    
    trigger_status = check_custom_triggers()
    if trigger_status:
        logging.info("A trigger has been activated.")
    
    snapshot = log_snapshot()
    if snapshot:
        logging.info("System snapshot:\n" + snapshot)

    logging.info("System check completed.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Logging Setup**: The script uses Python's `logging` module to log information, errors, and system states to a file named `system_reboot_log.log`.

2. **Checking Reboots**: It uses the `last reboot` command to log recent system reboots.

3. **Checking Custom Triggers**: This function should be customized based on specific triggers relevant to your system. The example provided checks for the existence of a file.

4. **Logging System Snapshots**: The script captures and logs a snapshot of current system processes using `ps aux`.

5. **Main Function**: Orchestrates the calling of other functions and logs their outputs.

This script needs to be run with appropriate permissions to execute system commands and may need to be adapted based on specific system configurations and requirements.
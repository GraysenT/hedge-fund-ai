Below is an example Python script that can be used to monitor and automatically restart crashed services or daemons on a Linux system. This script uses the `subprocess` module to manage system processes and the `time` module to handle periodic checks.

```python
import subprocess
import time

# List of services to monitor
services = [
    'apache2',
    'mysql',
    'ssh'
]

def check_service(service):
    """Check the status of a service using systemctl."""
    try:
        # Check the status of the service
        result = subprocess.run(['systemctl', 'is-active', service], text=True, capture_output=True)
        # If the service is not active, try to restart it
        if result.stdout.strip() != 'active':
            print(f"{service} is down. Attempting to restart...")
            restart_service(service)
        else:
            print(f"{service} is running normally.")
    except Exception as e:
        print(f"Failed to check status of {service}: {e}")

def restart_service(service):
    """Attempt to restart a service using systemctl."""
    try:
        # Restart the service
        subprocess.run(['systemctl', 'restart', service], check=True)
        print(f"{service} has been restarted.")
    except subprocess.CalledProcessError:
        print(f"Failed to restart {service}.")

def main():
    while True:
        for service in services:
            check_service(service)
        # Wait for 60 seconds before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()
```

### How It Works:
1. **Service List**: Define the services you want to monitor in the `services` list.
2. **Check Service**: The `check_service` function uses `systemctl is-active` to check if a service is running. If it's not active, it calls `restart_service`.
3. **Restart Service**: The `restart_service` function uses `systemctl restart` to restart the service.
4. **Main Loop**: The script continuously checks each service in a loop with a 60-second pause between checks.

### Requirements:
- This script is designed for systems that use `systemctl` (like most modern Linux distributions).
- It needs to be run with sufficient permissions to manage services, typically as root or using sudo.

### Usage:
- You can run this script on your server where it will continuously monitor and attempt to restart the specified services if they crash.
- To handle more complex scenarios or multiple servers, consider integrating with a proper monitoring tool or infrastructure management service.
```python
import datetime

def write_closure_log(agent_id, status, details):
    """
    Writes a closure log for a dead agent or a failed logic epoch.

    Args:
    agent_id (str): Unique identifier for the agent.
    status (str): Status of the agent or logic epoch ('deceased' or 'failed').
    details (str): Detailed description of the reason for the status.

    Returns:
    None
    """
    # Define the file name based on the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"closure_log_{timestamp}.txt"
    
    # Create and write to the log file
    with open(filename, 'w') as file:
        file.write(f"Closure Log for Agent/Epoch: {agent_id}\n")
        file.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Status: {status}\n")
        file.write(f"Details: {details}\n")
    
    print(f"Log written to {filename}")

# Example usage:
write_closure_log("Agent001", "deceased", "Agent lost during the mission due to critical system failure.")
write_closure_log("Epoch47", "failed", "Logic epoch failed due to an unhandled exception in processing.")
```

This Python script defines a function `write_closure_log` that creates a log file detailing the status of an agent or a logic epoch. Each log includes a timestamp, the agent's ID, the status (either 'deceased' for agents or 'failed' for logic epochs), and a detailed description of the reason for the status. The logs are saved to text files with names based on the current date and time.
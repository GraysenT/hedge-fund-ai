Here's a Python script that uses the `subprocess` module to run `evolve.py` and `runloop.py` in the background, restarting them if they fail, and logging each cycle of execution. The script uses an infinite loop to keep the processes running and checks their exit status to determine if a restart is necessary.

```python
import subprocess
import time
import logging

# Setup logging
logging.basicConfig(filename='process_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def run_script(script_name):
    """Run a script continuously, restarting on failure."""
    while True:
        logging.info(f"Starting {script_name}")
        # Start the process
        process = subprocess.Popen(['python', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for the process to complete
        stdout, stderr = process.communicate()
        
        # Log output and errors
        if process.returncode == 0:
            logging.info(f"{script_name} completed successfully.")
        else:
            logging.error(f"{script_name} failed with error: {stderr.decode().strip()}")
        
        # Log that we are restarting the script
        logging.info(f"Restarting {script_name}")
        time.sleep(1)  # Sleep for a short time before restarting to avoid hammering the system

if __name__ == '__main__':
    # Run evolve.py and runloop.py in separate background threads
    from threading import Thread
    
    evolve_thread = Thread(target=run_script, args=('evolve.py',))
    runloop_thread = Thread(target=run_script, args=('runloop.py',))
    
    # Start the threads
    evolve_thread.start()
    runloop_thread.start()
    
    # Join the threads to the main thread
    evolve_thread.join()
    runloop_thread.join()
```

### Explanation:
1. **Logging Setup**: The script uses Python's `logging` module to log information about the process execution, including start, success, failure, and restart messages. Logs are written to `process_log.log`.

2. **run_script Function**: This function takes the name of a Python script and runs it in an infinite loop. It uses `subprocess.Popen` to execute the script and waits for it to complete. If the script fails (i.e., returns a non-zero exit code), it logs the error. The script is restarted regardless of whether it completes successfully or fails.

3. **Threading**: The script uses Python's `threading` module to run `evolve.py` and `runloop.py` concurrently in separate threads. This allows both scripts to be managed independently.

4. **Process Management**: Each script is continuously monitored and restarted in its respective thread. The `time.sleep(1)` call ensures that there is a slight delay before restarting a script, which can be useful to prevent rapid, repeated crashing from overwhelming the system.

This script ensures that both `evolve.py` and `runloop.py` are kept running indefinitely, with automatic restarts and logging in case of failures. Adjust the paths and names as necessary depending on your environment.
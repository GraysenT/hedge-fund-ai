```python
import threading
import time

def monitor_thread_activity(threads, timeout):
    """
    Monitor threads to see if they are stuck in an infinite loop.

    Args:
    threads (list): List of threading.Thread objects.
    timeout (int): Time in seconds after which a thread is considered stuck.
    """
    start_time = {thread: time.time() for thread in threads}

    while True:
        for thread in threads:
            if thread.is_alive():
                runtime = time.time() - start_time[thread]
                if runtime > timeout:
                    print(f"Thread {thread.name} might be stuck in an infinite loop.")
            else:
                # Reset the timer if the thread has finished and restarted
                start_time[thread] = time.time()
        time.sleep(1)

def example_function():
    """
    Example function that might get stuck in an infinite loop.
    """
    while True:
        # Simulate some work
        time.sleep(0.1)

# Create threads
threads = [threading.Thread(target=example_function, name=f"Thread-{i}") for i in range(5)]

# Start threads
for thread in threads:
    thread.start()

# Monitor threads
monitor_thread_activity(threads, timeout=10)
```
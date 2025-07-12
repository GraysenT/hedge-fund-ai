```python
import threading

# Define a global lock to prevent concurrent execution and potential recursion issues
lock = threading.Lock()

def critical_function(data):
    """
    A critical function that modifies core logic or memory.
    This function is protected with a lock to prevent recursive calls that might
    lead to erasing core logic or memory.
    """
    with lock:
        # Simulate modifying core logic or memory
        print(f"Processing data: {data}")
        # Prevent recursive calls by checking the lock status
        if not lock.locked():
            raise Exception("Recursive call detected!")
        # Perform operations safely here
        data += 1
        print(f"Data processed: {data}")

def main():
    # Example data
    data = 10
    try:
        critical_function(data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
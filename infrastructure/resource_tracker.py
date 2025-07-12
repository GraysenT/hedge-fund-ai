To monitor memory, CPU, and bandwidth load from agents and modules in Python, you can use libraries like `psutil` for CPU and memory monitoring and `pandas` for data handling. For bandwidth monitoring, you can use `psutil` to track network statistics.

Here's a Python script that sets up basic monitoring for these resources:

```python
import psutil
import time
import pandas as pd

def get_cpu_usage():
    """ Returns the CPU usage percentage. """
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """ Returns memory usage statistics. """
    memory = psutil.virtual_memory()
    return {
        "total_memory": memory.total,
        "used_memory": memory.used,
        "percentage": memory.percent
    }

def get_bandwidth_usage(prev_net_io):
    """ Returns the network bandwidth usage. """
    new_net_io = psutil.net_io_counters()
    if prev_net_io:
        sent = new_net_io.bytes_sent - prev_net_io.bytes_sent
        recv = new_net_io.bytes_recv - prev_net_io.bytes_recv
    else:
        sent, recv = 0, 0
    return sent, recv, new_net_io

def monitor_system(interval=1):
    """ Monitors and logs the system's CPU, memory, and bandwidth usage at specified intervals. """
    prev_net_io = psutil.net_io_counters()
    data = []

    try:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            sent, recv, prev_net_io = get_bandwidth_usage(prev_net_io)

            # Log the current statistics
            stats = {
                "time": pd.Timestamp.now(),
                "cpu_usage": cpu_usage,
                "total_memory": memory_usage["total_memory"],
                "used_memory": memory_usage["used_memory"],
                "memory_usage_percent": memory_usage["percentage"],
                "bandwidth_sent": sent,
                "bandwidth_recv": recv
            }
            data.append(stats)
            print(stats)

            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        return pd.DataFrame(data)

if __name__ == "__main__":
    df = monitor_system()
    print(df)
```

### Explanation:
1. **CPU Usage**: The `get_cpu_usage` function uses `psutil.cpu_percent` to get the CPU usage percentage over a specified interval.
2. **Memory Usage**: The `get_memory_usage` function retrieves total, used, and percentage of memory usage using `psutil.virtual_memory`.
3. **Bandwidth Usage**: The `get_bandwidth_usage` function calculates the bytes sent and received since the last call, which gives an idea of the network bandwidth usage.
4. **Monitoring Loop**: The `monitor_system` function runs an infinite loop, collecting and printing these statistics at the specified interval. It can be stopped with a KeyboardInterrupt, and it returns a DataFrame with the collected data for further analysis or storage.

### Requirements:
- Install `psutil` and `pandas` using pip if not already installed:
  ```bash
  pip install psutil pandas
  ```

This script will continuously monitor and print the system's CPU, memory, and bandwidth usage until manually stopped. Adjust the `interval` parameter as needed to change the frequency of monitoring.
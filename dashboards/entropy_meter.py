```python
import psutil
import time
import os

def get_system_entropy():
    # This function will simulate system disorder by calculating CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    total_disorder = cpu_usage + memory_usage
    return total_disorder

def get_system_logic_churn():
    # This function will simulate logic churn by counting the number of processes and threads
    num_processes = len(psutil.pids())
    total_threads = sum([p.num_threads() for p in psutil.process_iter(attrs=['num_threads']) if 'num_threads' in p.info])
    logic_churn = num_processes + total_threads
    return logic_churn

def display_system_metrics():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        disorder = get_system_entropy()
        churn = get_system_logic_churn()
        print(f"System Total Disorder: {disorder:.2f}%")
        print(f"System Logic Churn: {churn}")
        time.sleep(1)

if __name__ == "__main__":
    display_system_metrics()
```

This Python script continuously monitors and displays the "total system disorder" and "logic churn" in real time. The disorder is calculated as the sum of CPU and memory usage percentages, and the churn is calculated as the sum of the number of processes and threads running on the system. The script updates these metrics every second.
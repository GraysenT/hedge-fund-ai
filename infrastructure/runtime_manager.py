```python
import threading
import time
import psutil
import os

class ThreadMonitor:
    def __init__(self):
        self.threads = []
        self.running = True

    def add_thread(self, target, args=()):
        thread = threading.Thread(target=target, args=args)
        thread.start()
        self.threads.append(thread)

    def monitor_threads(self):
        while self.running:
            for thread in self.threads:
                if not thread.is_alive():
                    print(f"Thread {thread.name} has stopped.")
                    self.threads.remove(thread)
            time.sleep(1)

    def monitor_memory(self):
        process = psutil.Process(os.getpid())
        while self.running:
            mem_info = process.memory_info()
            print(f"Memory Usage: RSS = {mem_info.rss / (1024 * 1024):.2f} MB; VMS = {mem_info.vms / (1024 * 1024):.2f} MB")
            time.sleep(5)

    def stop_monitoring(self):
        self.running = False
        for thread in self.threads:
            thread.join()
        print("All threads have been stopped and joined.")

def example_task(duration):
    print(f"Task starting; running for {duration} seconds.")
    time.sleep(duration)
    print("Task completed.")

if __name__ == "__main__":
    monitor = ThreadMonitor()
    monitor.add_thread(target=example_task, args=(10,))
    monitor.add_thread(target=example_task, args=(15,))

    # Start monitoring threads and memory in separate threads
    threading.Thread(target=monitor.monitor_threads).start()
    threading.Thread(target=monitor.monitor_memory).start()

    # Wait for all tasks to complete
    time.sleep(20)
    monitor.stop_monitoring()
```
```python
import time
from threading import Thread

class SentienceMonitor:
    def __init__(self):
        self.observation_data = []
        self.is_monitoring = False

    def start_monitoring(self):
        self.is_monitoring = True
        self.monitor_thread = Thread(target=self.monitor_behavior)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.is_monitoring = False
        self.monitor_thread.join()

    def monitor_behavior(self):
        while self.is_monitoring:
            data = self.collect_data()
            if self.analyze_data(data):
                self.report_sentience()
            time.sleep(1)  # Adjust the sleep time as needed

    def collect_data(self):
        # Simulate data collection
        import random
        data = {
            'complexity': random.randint(1, 100),
            'novelty': random.randint(1, 100),
            'self_modification': random.choice([True, False]),
            'goal_oriented': random.choice([True, False])
        }
        return data

    def analyze_data(self, data):
        # Define thresholds for sentience indicators
        thresholds = {
            'complexity': 75,
            'novelty': 70,
            'self_modification': True,
            'goal_oriented': True
        }

        if (data['complexity'] > thresholds['complexity'] and
            data['novelty'] > thresholds['novelty'] and
            data['self_modification'] == thresholds['self_modification'] and
            data['goal_oriented'] == thresholds['goal_oriented']):
            return True
        return False

    def report_sentience(self):
        print("Warning: Signs of full sentient behavior detected.")

if __name__ == "__main__":
    monitor = SentienceMonitor()
    monitor.start_monitoring()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop_monitoring()
        print("Monitoring stopped.")
```

This Python script defines a `SentienceMonitor` class that simulates monitoring for signs of full sentient behavior in an experimental setup. The `monitor_behavior` method collects data periodically, analyzes it for signs of sentience, and reports if certain thresholds are met. The monitoring runs in a separate thread, allowing the main program to perform other tasks or simply wait until the user decides to stop the monitoring.
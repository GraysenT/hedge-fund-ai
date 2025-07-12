```python
import threading
import time
import random

class IntelligenceMetrics:
    def __init__(self):
        self.intelligence_depth = 0
        self.recursion_loops = 0
        self.independence = 0

    def update_metrics(self):
        while True:
            self.intelligence_depth = random.randint(1, 100)
            self.recursion_loops = random.randint(0, 10)
            self.independence = random.randint(0, 5)
            time.sleep(1)

    def get_metrics(self):
        return {
            'intelligence_depth': self.intelligence_depth,
            'recursion_loops': self.recursion_loops,
            'independence': self.independence
        }

def metrics_monitor(metrics):
    while True:
        current_metrics = metrics.get_metrics()
        print(f"Intelligence Depth: {current_metrics['intelligence_depth']}, "
              f"Recursion Loops: {current_metrics['recursion_loops']}, "
              f"Independence: {current_metrics['independence']}")
        time.sleep(1)

if __name__ == "__main__":
    metrics = IntelligenceMetrics()
    threading.Thread(target=metrics.update_metrics, daemon=True).start()
    metrics_monitor(metrics)
```
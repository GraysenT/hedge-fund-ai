import time
from queue import PriorityQueue

class LatencyAwareSignalQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_signal(self, signal):
        latency = signal.get("latency", 50)  # milliseconds
        self.queue.put((latency, time.time(), signal))
        print(f"[QUEUE] Signal added with latency: {latency}ms")

    def get_next(self):
        if not self.queue.empty():
            latency, _, signal = self.queue.get()
            print(f"[QUEUE] Signal dispatched: {signal}")
            return signal
        return None
import time

class LatencyProfiler:
    def __init__(self):
        self.logs = []

    def profile(self, label, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = round((end - start) * 1000, 3)  # milliseconds
        self.logs.append((label, duration))
        print(f"[LATENCY] {label}: {duration} ms")
        return result

    def get_logs(self):
        return self.logs
import time

class RecursionTracker:
    def __init__(self, threshold=50, cooldown_seconds=2):
        self.calls = {}
        self.threshold = threshold
        self.cooldown = cooldown_seconds

    def track(self, label):
        now = time.time()
        history = self.calls.get(label, [])
        history = [t for t in history if now - t < self.cooldown]
        history.append(now)
        self.calls[label] = history
        if len(history) > self.threshold:
            return False  # recursion likely
        return True

    def reset(self, label):
        self.calls[label] = []
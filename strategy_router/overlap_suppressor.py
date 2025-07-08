from collections import defaultdict

class OverlapSuppressor:
    def __init__(self):
        self.recent_signals = defaultdict(list)

    def register(self, signal):
        key = signal["symbol"]
        self.recent_signals[key].append(signal)

    def suppress_if_duplicate(self, signal):
        key = signal["symbol"]
        if any(s["strategy"] != signal["strategy"] and s["action"] == signal["action"] for s in self.recent_signals[key]):
            print(f"[SUPPRESS] Overlap detected on {key}, signal suppressed.")
            return True
        return False
class CrowdNoiseFilter:
    def __init__(self):
        self.muted = []

    def filter(self, signal):
        if "Reddit" in signal.get("source", "") or "Twitter" in signal.get("source", ""):
            if signal.get("confidence", 0) < 0.7:
                self.muted.append(signal)
                print(f"[NOISE FILTER] Muted crowd-sourced signal: {signal}")
                return True
        return False

    def get_muted(self):
        return self.muted
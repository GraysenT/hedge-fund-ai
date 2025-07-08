class DarkPoolSignalDetector:
    def __init__(self):
        self.alerts = []

    def detect(self, volume, avg_volume, price_spread):
        if volume > 2 * avg_volume and price_spread < 0.001:
            alert = "Dark pool activity spike detected"
            self.alerts.append(alert)
            print(f"[DARK POOL DETECTOR] {alert}")
            return True
        return False
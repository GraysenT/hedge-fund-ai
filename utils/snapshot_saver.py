import os
import csv
from datetime import datetime

class SnapshotSaver:
    def __init__(self, path="snapshots/allocation_history.csv"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["date", "strategy", "weight", "status"])

    def save(self, weights: dict, muted: list):
        today = datetime.now().strftime("%Y-%m-%d")
        with open(self.path, mode='a', newline='') as f:
            writer = csv.writer(f)
            for strat, weight in weights.items():
                status = "Muted" if strat in muted else "Active"
                writer.writerow([today, strat, round(weight, 6), status])

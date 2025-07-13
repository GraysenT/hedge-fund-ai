import csv
from datetime import datetime

class PerformanceLogger:
    def __init__(self, file_path="logs/performance_log.csv"):
        self.file_path = file_path
        with open(self.file_path, mode='a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "strategy", "pnl", "sharpe"])

    def log(self, strategy_name, pnl, sharpe):
        with open(self.file_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.utcnow(), strategy_name, pnl, sharpe])
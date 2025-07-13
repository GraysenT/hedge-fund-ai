import csv
from datetime import datetime

class SignalRecorder:
    def __init__(self, file="logs/signal_log.csv"):
        self.file = file
        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time", "strategy", "symbol", "signal", "price"])

    def log(self, strategy_name, symbol, signal, price):
        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.utcnow(), strategy_name, symbol, signal, price])
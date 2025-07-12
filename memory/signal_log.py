import csv
import time

class SignalLogger:
    def __init__(self, log_file="signal_log.csv"):
        self.log_file = log_file
        with open(self.log_file, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "symbol", "action", "confidence", "result"])

    def log_signal(self, signal, result="pending"):
        with open(self.log_file, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([
                time.strftime('%Y-%m-%d %H:%M:%S'),
                signal.get("symbol"),
                signal.get("action"),
                signal.get("confidence"),
                result
            ])

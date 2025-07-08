import time

class NewsDelayTracker:
    def __init__(self):
        self.delays = []

    def track(self, news_time, signal_time):
        delay = signal_time - news_time
        self.delays.append(delay)
        print(f"[NEWS DELAY] Propagation time: {delay:.2f} seconds")
        return delay

    def get_avg_delay(self):
        if not self.delays:
            return 0.0
        return sum(self.delays) / len(self.delays)
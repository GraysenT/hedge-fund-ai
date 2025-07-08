class TimeRewardAdjuster:
    def __init__(self, fast_window=3, slow_window=10):
        self.fast_window = fast_window
        self.slow_window = slow_window

    def adjust_reward(self, recent_returns):
        if len(recent_returns) < self.slow_window:
            return 1.0

        fast_avg = sum(recent_returns[-self.fast_window:]) / self.fast_window
        slow_avg = sum(recent_returns[-self.slow_window:]) / self.slow_window

        multiplier = 1.0
        if fast_avg > slow_avg:
            multiplier += 0.25
        elif fast_avg < slow_avg:
            multiplier -= 0.25

        print(f"[REWARD ADJ] Fast avg = {fast_avg:.3f}, Slow avg = {slow_avg:.3f}, Multiplier = {multiplier:.2f}")
        return multiplier
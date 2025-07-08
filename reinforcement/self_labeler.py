class StrategySelfLabeler:
    def __init__(self):
        self.labels = {}

    def label(self, performance_data):
        for strategy, stats in performance_data.items():
            if stats['sharpe'] > 1.5 and stats['drawdown'] < 0.1:
                label = "Stable High Performer"
            elif stats['volatility'] > 0.3:
                label = "Aggressive Trader"
            elif stats['return'] < 0:
                label = "Underperforming"
            else:
                label = "Neutral"

            self.labels[strategy] = label
            print(f"[SELF LABEL] {strategy} → {label}")
        return self.labels
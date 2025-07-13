import numpy as np

class TimeReversedTrainer:
    def train(self, price_series):
        reversed_prices = price_series[::-1]
        labels = np.sign(np.diff(reversed_prices))
        signals = []

        for i in range(len(labels)):
            if labels[i] > 0:
                signals.append("buy")
            elif labels[i] < 0:
                signals.append("sell")
            else:
                signals.append("hold")

        print("⏪ Time-Reversed Strategy Generated")
        return signals[::-1]  # Flip back to original direction
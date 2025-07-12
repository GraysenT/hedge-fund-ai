# strategies/macro_sniper.py

import numpy as np

class MacroSniper:
    def __init__(self, overnight_signals, hedger_behavior):
        self.overnight_signals = overnight_signals
        self.hedger_behavior = hedger_behavior

    def calculate_signal(self):
        """
        Calculate the signal based on overnight signals and hedger behavior.
        """
        return np.mean(self.overnight_signals) * np.mean(self.hedger_behavior)

    def execute_strategy(self):
        """
        Execute the strategy based on the calculated signal.
        """
        signal = self.calculate_signal()

        if signal > 0:
            return 'Buy'
        elif signal < 0:
            return 'Sell'
        else:
            return 'Hold'

    def update_signals(self, new_overnight_signals, new_hedger_behavior):
        """
        Update the overnight signals and hedger behavior.
        """
        self.overnight_signals = new_overnight_signals
        self.hedger_behavior = new_hedger_behavior

def generate_signal():
    return 'skip'

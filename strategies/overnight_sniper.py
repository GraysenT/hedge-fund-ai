# strategies/overnight_sniper.py

import pandas as pd
from datetime import datetime, timedelta
from pytz import timezone

class OvernightSniper:
    def __init__(self, fed_day_signals, scalper_behavior):
        self.fed_day_signals = fed_day_signals
        self.scalper_behavior = scalper_behavior

    def get_fed_day_signals(self, date):
        return self.fed_day_signals[date]

    def get_scalper_behavior(self, date):
        return self.scalper_behavior[date]

    def blend_signals(self, date):
        fed_day_signal = self.get_fed_day_signals(date)
        scalper_behavior = self.get_scalper_behavior(date)
        blended_signal = (fed_day_signal + scalper_behavior) / 2
        return blended_signal

    def execute_strategy(self):
        current_date = datetime.now(timezone('US/Eastern')).date()
        blended_signal = self.blend_signals(current_date)

        if blended_signal > 0:
            return 'Buy'
        elif blended_signal < 0:
            return 'Sell'
        else:
            return 'Hold'
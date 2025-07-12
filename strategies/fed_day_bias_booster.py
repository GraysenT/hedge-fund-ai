# strategies/fed_day_bias_booster.py

import pandas as pd
from datetime import datetime, timedelta

class FedDayBiasBooster:
    def __init__(self, data):
        self.data = data
        self.fed_days = self.get_fed_days()

    def get_fed_days(self):
        fed_days = []
        for date in self.data['Date']:
            if date.weekday() == 2 and (14 <= date.day <= 21):
                fed_days.append(date)
        return fed_days

    def apply_booster(self):
        boosted_data = self.data.copy()
        for i in range(len(boosted_data)):
            if boosted_data.loc[i, 'Date'] in self.fed_days:
                boosted_data.loc[i, 'Close'] *= 1.02
        return boosted_data

    def backtest(self):
        boosted_data = self.apply_booster()
        initial_investment = 10000
        shares = initial_investment / boosted_data.loc[0, 'Close']
        final_portfolio = shares * boosted_data.loc[-1, 'Close']
        return final_portfolio - initial_investment

def generate_signal():
    return 'skip'

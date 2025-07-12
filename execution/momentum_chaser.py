import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Union

class MomentumChaser:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def calculate_momentum(self, period: int) -> pd.Series:
        return self.data['Close'].diff(period) / self.data['Close'].shift(period)

    def identify_breakouts(self, momentum: pd.Series, threshold: float) -> pd.Series:
        return (momentum > threshold)

    def execute_trades(self, breakouts: pd.Series) -> List[Dict[str, Union[datetime, str, float]]]:
        trades = []
        for date, is_breakout in breakouts.iteritems():
            if is_breakout:
                trades.append({
                    'Date': date,
                    'Action': 'Buy',
                    'Price': self.data.loc[date, 'Close']
                })
                sell_date = date + timedelta(days=1)
                if sell_date in self.data.index:
                    trades.append({
                        'Date': sell_date,
                        'Action': 'Sell',
                        'Price': self.data.loc[sell_date, 'Close']
                    })
        return trades

    def chase_momentum(self, period: int, threshold: float) -> List[Dict[str, Union[datetime, str, float]]]:
        momentum = self.calculate_momentum(period)
        breakouts = self.identify_breakouts(momentum, threshold)
        trades = self.execute_trades(breakouts)
        return trades
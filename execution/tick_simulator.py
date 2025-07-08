import pandas as pd
import numpy as np
import time
import random

class TickExecutionSimulator:
    def __init__(self, slippage_model='normal', tick_delay_range=(0.01, 0.2), seed=None):
        self.slippage_model = slippage_model
        self.tick_delay_range = tick_delay_range
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def simulate_trade(self, signal, tick_data):
        """
        Simulate execution of a signal on tick-level data.
        Args:
            signal: dict with 'asset', 'direction', 'confidence', 'timestamp'
            tick_data: DataFrame with tick-level prices (columns: ['timestamp', 'price'])

        Returns:
            dict with executed trade details
        """
        if tick_data.empty:
            return {"status": "fail", "reason": "no tick data"}

        # Simulate delay in reaction to signal
        delay = random.uniform(*self.tick_delay_range)
        signal_time = pd.to_datetime(signal['timestamp'])
        execution_time = signal_time + pd.to_timedelta(delay, unit='s')

        # Get closest tick after execution_time
        executed_tick = tick_data[tick_data['timestamp'] >= execution_time]
        if executed_tick.empty:
            return {"status": "fail", "reason": "no tick after delay"}

        tick = executed_tick.iloc[0]
        price = tick['price']

        # Apply slippage
        slippage = self._simulate_slippage()
        if signal['direction'] == 'buy':
            exec_price = price + slippage
        elif signal['direction'] == 'sell':
            exec_price = price - slippage
        else:
            return {"status": "fail", "reason": "invalid direction"}

        return {
            "status": "executed",
            "asset": signal['asset'],
            "direction": signal['direction'],
            "confidence": signal['confidence'],
            "signal_time": signal_time,
            "execution_time": tick['timestamp'],
            "execution_price": exec_price,
            "delay_sec": delay,
            "slippage": slippage
        }

    def _simulate_slippage(self):
        if self.slippage_model == 'normal':
            return np.abs(np.random.normal(loc=0.001, scale=0.002))
        elif self.slippage_model == 'fixed':
            return 0.001
        else:
            return 0.0

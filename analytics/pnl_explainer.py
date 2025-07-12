# analytics/pnl_explainer.py

import pandas as pd
import numpy as np

class PnLExplainer:
    def __init__(self, data):
        self.data = data

    def calculate_signal_pnl(self):
        """
        Calculate PnL based on signal
        """
        self.data['signal_pnl'] = self.data['signal'] * self.data['returns']
        return self.data['signal_pnl']

    def calculate_strategy_pnl(self):
        """
        Calculate PnL based on strategy
        """
        self.data['strategy_pnl'] = self.data['strategy'] * self.data['returns']
        return self.data['strategy_pnl']

    def calculate_execution_pnl(self):
        """
        Calculate PnL based on execution
        """
        self.data['execution_pnl'] = self.data['execution'] * self.data['returns']
        return self.data['execution_pnl']

    def calculate_total_pnl(self):
        """
        Calculate total PnL
        """
        self.data['total_pnl'] = self.data['signal_pnl'] + self.data['strategy_pnl'] + self.data['execution_pnl']
        return self.data['total_pnl']

# Example usage
if __name__ == "__main__":
    # Create a sample dataframe
    data = pd.DataFrame({
        'signal': np.random.randint(-1, 2, 100),
        'strategy': np.random.randint(-1, 2, 100),
        'execution': np.random.randint(-1, 2, 100),
        'returns': np.random.normal(0, 1, 100)
    })

    explainer = PnLExplainer(data)

    print("Signal PnL: ", explainer.calculate_signal_pnl())
    print("Strategy PnL: ", explainer.calculate_strategy_pnl())
    print("Execution PnL: ", explainer.calculate_execution_pnl())
    print("Total PnL: ", explainer.calculate_total_pnl())
    

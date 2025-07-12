import pandas as pd

class FuturesBacktestEngine:
    def __init__(self, data, leverage=10, margin_requirement=0.1, strategy=None):
        self.data = data  # Data should be a dataframe with futures price history
        self.leverage = leverage
        self.margin_requirement = margin_requirement
        self.strategy = strategy  # A specific strategy object
        self.results = []

    def simulate_trade(self, entry_price, exit_price, contract_size, position_type="long"):
        """Simulate a futures trade considering leverage and margin."""
        margin = entry_price * contract_size * self.margin_requirement
        leverage_amount = margin * self.leverage
        pnl = (exit_price - entry_price) * contract_size if position_type == "long" else (entry_price - exit_price) * contract_size
        trade_result = {"entry_price": entry_price, "exit_price": exit_price, "pnl": pnl, "margin": margin, "leverage_used": leverage_amount}
        self.results.append(trade_result)
        print(f"Trade result: Entry: {entry_price}, Exit: {exit_price}, PnL: {pnl}, Leverage Used: {leverage_amount}")
        return pnl

    def backtest_strategy(self):
        """Backtest using the strategy defined in the engine."""
        for index, row in self.data.iterrows():
            entry_price = row['entry_price']
            exit_price = row['exit_price']
            contract_size = row['contract_size']
            position_type = self.strategy.combine_signals(row)  # Using combined strategy to generate signal
            self.simulate_trade(entry_price, exit_price, contract_size, position_type)
        
        total_pnl = sum([trade['pnl'] for trade in self.results])
        print(f"Total PnL from backtest: {total_pnl}")
        return total_pnl

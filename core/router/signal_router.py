from core.trade_executor import TradeExecutor
from core.portfolio_manager import PortfolioManager
from utils.logger import log

class SignalRouter:
    def __init__(self, executor: TradeExecutor, portfolio: PortfolioManager):
        self.executor = executor
        self.portfolio = portfolio

    def route(self, symbol, signal, price):
        size = 1
        if signal == "buy" or signal == "sell":
            self.executor.execute_trade(symbol, signal, size)
            self.portfolio.update_position(symbol, signal, size, price)
            log.info(f"✅ Executed {signal} for {symbol} at {price}")
from core.strategy_registry import StrategyRegistry
from core.market_data_feed import MarketDataFeed
from core.trade_executor import TradeExecutor
from core.portfolio_manager import PortfolioManager
from core.strategy_performance import StrategyPerformance
from evolution.evolution_engine import EvolutionEngine

import time

def initialize_system():
    registry = StrategyRegistry("strategies")
    registry.discover_strategies()
    strategies = [cls(name=cls.__name__, parameters={"base": 1}) for cls in registry.get_all()]

    data_feed = MarketDataFeed(data_sources=["alpaca", "binance"])
    portfolio = PortfolioManager()
    broker_api = MockBrokerAPI()
    executor = TradeExecutor(broker_api)
    tracker = StrategyPerformance()
    evolution = EvolutionEngine(strategies)

    return strategies, data_feed, portfolio, executor, tracker, evolution

class MockBrokerAPI:
    def buy(self, symbol, size): print(f"Buying {size} of {symbol}")
    def sell(self, symbol, size): print(f"Selling {size} of {symbol}")

if __name__ == "__main__":
    strategies, data_feed, portfolio, executor, tracker, evolution = initialize_system()
    symbol = "AAPL"

    while True:
        market_data = data_feed.fetch(symbol)

        # 1. Select and run strategy
        strategy = evolution.select_strategy()
        signal = strategy.generate_signal(market_data)

        # 2. Execute trade
        if signal in ["buy", "sell"]:
            executor.execute_trade(symbol, signal, size=10)
            portfolio.update_position(symbol, signal, 10, market_data["price"])

        # 3. Simulated performance update
        pnl = market_data["price"] * 0.01  # Fake PnL
        tracker.update(strategy.name, pnl, sharpe=1.0)
        strategy.score(pnl, 1.0)
        evolution.update_rewards(strategy.name, pnl)

        # 4. Periodically evolve strategy set
        if int(time.time()) % 60 == 0:
            evolution.run_generation()

        time.sleep(1)
from core.market_data_feed import MarketDataFeed
from core.trade_executor import TradeExecutor
from core.portfolio_manager import PortfolioManager
from core.strategy_performance import StrategyPerformance
from evolution.evolution_engine import EvolutionEngine
from strategies.trend_following import TrendFollowingStrategy
from strategies.mean_reversion import MeanReversionStrategy

def run_simulation():
    strategies = [
        TrendFollowingStrategy("TrendFollowing", {"base": 1}),
        MeanReversionStrategy("MeanReversion", {"base": 1})
    ]
    data_feed = MarketDataFeed(["sim"])
    executor = TradeExecutor(MockBroker())
    portfolio = PortfolioManager()
    tracker = StrategyPerformance()
    evolution = EvolutionEngine(strategies)

    for _ in range(100):
        data = {"price": 100 + (_ % 10), "ma": 105, "upper_band": 110, "lower_band": 95, "recent_high": 108, "recent_low": 92}
        strategy = evolution.select_strategy()
        signal = strategy.generate_signal(data)

        if signal != "hold":
            executor.execute_trade("SIM", signal, 1)
            portfolio.update_position("SIM", signal, 1, data["price"])

        tracker.update(strategy.name, 0.1, 1.0)
        strategy.score(0.1, 1.0)
        evolution.update_rewards(strategy.name, 0.1)

    print(tracker.all_stats())

class MockBroker:
    def buy(self, symbol, qty): print(f"[SIM BUY] {symbol}: {qty}")
    def sell(self, symbol, qty): print(f"[SIM SELL] {symbol}: {qty}")

if __name__ == "__main__":
    run_simulation()
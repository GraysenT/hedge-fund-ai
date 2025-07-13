from evolution.rl_controller import RLController
from core.market_data_feed import MarketDataFeed
from strategies.trend_following import TrendFollowingStrategy
import random

class LiveRLTrainer:
    def __init__(self):
        self.strategy = TrendFollowingStrategy("Trend", {"base": 1})
        self.rl = RLController([self.strategy])
        self.data_feed = MarketDataFeed(["yfinance"])

    def run(self):
        for _ in range(100):
            market_data = self.data_feed.fetch("AAPL")
            signal = self.strategy.generate_signal(market_data)
            reward = random.uniform(-0.3, 1.0)  # TODO: link to real PnL tracker
            self.rl.update(self.strategy.name, reward)

if __name__ == "__main__":
    LiveRLTrainer().run()
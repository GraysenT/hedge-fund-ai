import time
import logging
from strategies.trend_following import TrendFollowing
from strategies.mean_reversion import MeanReversion
from strategies.momentum_based import MomentumBased
from strategies.breakout import Breakout
from strategies.macd import MACD
from strategies.bollinger_bands import BollingerBands
from backtesting.backtester import Backtester
from data_fetching.real_time_data import RealTimeData
from risk_management.risk_manager import RiskManager
from utils.performance_metrics import calculate_sharpe_ratio
from utils.strategy_optimizer import optimize_strategy

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Alpaca (or other API) for real-time data and execution
api_key = 'your_alpaca_api_key'
secret_key = 'your_alpaca_secret_key'
real_time_data = RealTimeData(api_key, secret_key)
risk_manager = RiskManager()

# Initialize strategies
strategies = [
    TrendFollowing(),
    MeanReversion(),
    MomentumBased(),
    Breakout(),
    MACD(),
    BollingerBands()
]

# Run the backtester
backtester = Backtester(strategies)
backtester.run_backtest()

# Run real-time trading loop
def run_trading_loop():
    while True:
        try:
            # Fetch live data for multiple assets (e.g., AAPL, BTC/USD)
            live_data = real_time_data.get_live_data(["AAPL", "BTCUSD"])

            # Choose strategy with the best signal
            signals = {}
            for strategy in strategies:
                signal = strategy.get_signal(live_data)
                signals[strategy.name] = signal
            
            # Select the best strategy based on the signals
            best_strategy = max(signals, key=signals.get)
            logging.info(f"Best Strategy: {best_strategy}")

            # Risk management: Calculate position size and execute trade
            position_size = risk_manager.calculate_position_size(live_data)
            risk_manager.place_trade(best_strategy, position_size)

            # Log performance
            sharpe_ratio = calculate_sharpe_ratio(live_data)
            logging.info(f"Sharpe Ratio: {sharpe_ratio}")

            # Wait for the next cycle
            time.sleep(60)

        except Exception as e:
            logging.error(f"Error in trading loop: {e}")
            time.sleep(60)

# Optimize strategies using hyperparameter optimization
def optimize_trading_strategies():
    for strategy in strategies:
        optimized_params = optimize_strategy(strategy)
        strategy.set_params(optimized_params)

# Run strategy optimization and trading loop
optimize_trading_strategies()
run_trading_loop()
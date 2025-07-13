from core.strategy_base import StrategyBase

class CryptoSpreadStrategy(StrategyBase):
    def generate_signal(self, market_data):
        price_binance = market_data.get("BTCUSD_BINANCE", {}).get("price", 0)
        price_coinbase = market_data.get("BTCUSD_COINBASE", {}).get("price", 0)
        spread = price_binance - price_coinbase

        if spread > 100:
            return "sell"
        elif spread < -100:
            return "buy"
        return "hold"
import alpaca_trade_api as tradeapi
import yfinance as yf
import requests
import pandas as pd

class RealTimeData:
    def __init__(self, api_key, secret_key, paper=True):
        self.api_key = api_key
        self.secret_key = secret_key
        self.paper = paper
        base_url = "https://paper-api.alpaca.markets" if paper else "https://api.alpaca.markets"
        self.api = tradeapi.REST(self.api_key, self.secret_key, base_url, api_version='v2')

    def get_historical_data(self, symbol, timeframe='day', limit=100):
        """Get historical data for stocks, commodities, ETFs, or cryptos."""
        if symbol in ["BTCUSD", "ETHUSD"]:  # If it's a crypto symbol
            return self.get_crypto_data(symbol, timeframe, limit)
        elif symbol.startswith("SPY") or symbol.startswith("QQQ"):  # Example ETF symbols
            return self.get_etf_data(symbol, timeframe, limit)
        else:  # Assume it's a stock or commodity
            return self.get_stock_or_commodity_data(symbol, timeframe, limit)
    
    def get_stock_or_commodity_data(self, symbol, timeframe='day', limit=100):
        """Get stock or commodity data using Yahoo Finance."""
        data = yf.download(symbol, period="1y", interval="1d")  # Use Yahoo Finance for stock/commodity data
        return data[['Open', 'High', 'Low', 'Close', 'Volume']].tail(limit)

    def get_etf_data(self, symbol, timeframe='day', limit=100):
        """Get ETF data using Yahoo Finance."""
        data = yf.download(symbol, period="1y", interval="1d")
        return data[['Open', 'High', 'Low', 'Close', 'Volume']].tail(limit)

    def get_crypto_data(self, symbol, timeframe='day', limit=100):
        """Get crypto data using the CoinGecko API."""
        url = f'https://api.coingecko.com/api/v3/coins/{symbol.lower()}/market_chart'
        params = {'vs_currency': 'usd', 'days': '365'}
        response = requests.get(url, params=params).json()
        data = pd.DataFrame(response['prices'], columns=['time', 'close'])
        data['time'] = pd.to_datetime(data['time'], unit='ms')
        data.set_index('time', inplace=True)
        data['Open'] = data['Low']  # Placeholder for Open price
        data['High'] = data['High']  # Placeholder for High price
        data['Low'] = data['Low']  # Placeholder for Low price
        data['Volume'] = 0  # Placeholder for Volume
        return data.tail(limit)

    def get_live_price(self, symbol):
        """Get real-time price for stocks, commodities, ETFs, or cryptos."""
        if symbol in ["BTCUSD", "ETHUSD"]:  # Crypto
            return self.get_crypto_live_price(symbol)
        else:  # Stocks, ETFs, and Commodities
            return self.get_stock_live_price(symbol)
    
    def get_stock_live_price(self, symbol):
        """Fetch live price for stocks and commodities."""
        # Updated method to use `get_latest_trade()` instead of `get_last_trade()`
        last_trade = self.api.get_latest_trade(symbol)
        return last_trade.price
    
    def get_crypto_live_price(self, symbol):
        """Fetch live price for crypto using the CoinGecko API."""
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd'
        response = requests.get(url).json()
        return response[symbol.lower()]['usd']
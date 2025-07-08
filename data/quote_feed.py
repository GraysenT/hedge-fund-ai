import os
from polygon import RESTClient
from dotenv import load_dotenv
import requests

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
client = RESTClient(POLYGON_API_KEY)

def get_crypto_price(symbol="bitcoin"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return {
            "ticker": symbol.upper(),
            "last": float(data[symbol]["usd"]),
            "bid": float(data[symbol]["usd"]),
            "ask": float(data[symbol]["usd"]),
            "source": "CoinGecko"
        }
    except Exception as e:
        print(f"❌ Failed to fetch crypto price for {symbol}: {e}")
        return None

def get_equity_price(ticker="AAPL"):
    try:
        quote = client.get_last_quote(ticker)
        return {
            "ticker": ticker.upper(),
            "last": (quote.askprice + quote.bidprice) / 2,
            "bid": quote.bidprice,
            "ask": quote.askprice,
            "source": "Polygon"
        }
    except Exception as e:
        print(f"❌ Failed to fetch quote for {ticker}: {e}")
        return None

def get_latest_price(ticker="AAPL"):
    ticker = ticker.upper()
    if ticker in ["BTC", "ETH", "SOL"]:
        return get_crypto_price(ticker.lower())
    else:
        return get_equity_price(ticker)

if __name__ == "__main__":
    print(get_latest_price("AAPL"))
    print(get_latest_price("BTC"))
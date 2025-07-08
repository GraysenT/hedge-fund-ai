import requests

def get_crypto_price(symbol="bitcoin"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        r = requests.get(url).json()
        return r[symbol]["usd"]
    except Exception as e:
        print(f"❌ Failed to fetch crypto price for {symbol}: {e}")
        return None
import yfinance as yf

def get_price(symbol):
    try:
        data = yf.download(symbol, period="1d", interval="1m")
        return float(data["Close"].iloc[-1])
    except Exception:
        return None
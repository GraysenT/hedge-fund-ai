from datetime import datetime, time
import pytz

def is_us_stock_market_open():
    now = datetime.now(pytz.timezone("US/Eastern"))
    weekday = now.weekday()
    market_open = time(9, 30)
    market_close = time(16, 0)
    return weekday < 5 and market_open <= now.time() <= market_close

def is_futures_market_open():
    now = datetime.now(pytz.timezone("US/Central"))
    weekday = now.weekday()
    hour = now.time().hour
    if weekday == 6:  # Sunday
        return now.time() >= time(17, 0)
    elif weekday == 5:  # Saturday
        return False
    else:
        return not (16 <= now.time().hour < 17)

def is_crypto_market_open():
    return True  # Crypto is 24/7

def get_market_status():
    return {
        "US Stocks": "Open" if is_us_stock_market_open() else "Closed",
        "Futures": "Open" if is_futures_market_open() else "Closed",
        "Crypto": "Open" if is_crypto_market_open() else "Closed",
    }

def get_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
from datetime import datetime, time
import pytz

class GlobalMarketHours:
    def __init__(self):
        self.exchanges = {
            "NYSE": {"timezone": "America/New_York", "open": time(9, 30), "close": time(16, 0)},
            "CME": {"timezone": "America/Chicago", "open": time(8, 30), "close": time(15, 0)},
            "LSE": {"timezone": "Europe/London", "open": time(8, 0), "close": time(16, 30)},
            "TSE": {"timezone": "Asia/Tokyo", "open": time(9, 0), "close": time(15, 0)},
            "Crypto": {"timezone": "UTC", "open": time(0, 0), "close": time(23, 59)},
        }

    def is_market_open(self, exchange: str, now=None):
        if exchange not in self.exchanges:
            return False
        info = self.exchanges[exchange]
        tz = pytz.timezone(info["timezone"])
        now = now or datetime.now(tz)
        open_time = tz.localize(datetime.combine(now.date(), info["open"]))
        close_time = tz.localize(datetime.combine(now.date(), info["close"]))
        return open_time <= now <= close_time

    def get_open_exchanges(self):
        open_ex = []
        for ex in self.exchanges:
            if self.is_market_open(ex):
                open_ex.append(ex)
        return open_ex

    def get_exchange_status(self):
        status = {}
        for ex in self.exchanges:
            status[ex] = self.is_market_open(ex)
        return status

    def get_current_local_times(self):
        local_times = {}
        for ex, info in self.exchanges.items():
            tz = pytz.timezone(info["timezone"])
            local_times[ex] = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return local_times

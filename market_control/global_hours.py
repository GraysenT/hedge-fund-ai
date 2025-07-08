from datetime import datetime, time
import pytz

def is_market_open(region):
    now_utc = datetime.utcnow()

    markets = {
        "US": {
            "timezone": "America/New_York",
            "open": time(9, 30),
            "close": time(16, 0),
            "weekdays": [0, 1, 2, 3, 4]
        },
        "EU": {
            "timezone": "Europe/Berlin",
            "open": time(8, 0),
            "close": time(16, 30),
            "weekdays": [0, 1, 2, 3, 4]
        },
        "Asia": {
            "timezone": "Asia/Tokyo",
            "open": time(9, 0),
            "close": time(15, 0),
            "weekdays": [0, 1, 2, 3, 4]
        },
        "Futures": {
            "timezone": "America/Chicago",  # CME timezone
            "open": time(17, 0),  # 5:00 PM
            "close": time(16, 0),  # 4:00 PM next day
            "weekdays": [6, 0, 1, 2, 3, 4]  # Sunday–Friday
        },
        "Crypto": {
            "timezone": "UTC",
            "open": time(0, 0),
            "close": time(23, 59),
            "weekdays": list(range(7))  # 0–6 = every day
        }
    }

    market = markets[region]
    local_time = now_utc.astimezone(pytz.timezone(market["timezone"]))
    is_open = (
        local_time.weekday() in market["weekdays"] and
        market["open"] <= local_time.time() <= market["close"]
    )
    return is_open

def get_market_status():
    regions = ["US", "EU", "Asia", "Futures", "Crypto"]
    status = {r: is_market_open(r) for r in regions}
    status["Any Open"] = any(status.values())
    return status

if __name__ == "__main__":
    status = get_market_status()
    for region, open_ in status.items():
        print(f"{region} market is {'OPEN ✅' if open_ else 'CLOSED ❌'}")
        
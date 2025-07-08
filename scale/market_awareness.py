import datetime
import pytz

MARKETS = {
    "US": "America/New_York",
    "EU": "Europe/London",
    "ASIA": "Asia/Tokyo",
    "LATAM": "America/Sao_Paulo",
    "CRYPTO": "UTC",
    "FUTURES": "UTC"
}

def get_market_status():
    now = datetime.datetime.utcnow()
    status = {}
    for region, tz in MARKETS.items():
        local = now.replace(tzinfo=datetime.timezone.utc).astimezone(pytz.timezone(tz))
        is_open = 8 <= local.hour < 17 if region != "CRYPTO" else True
        status[region] = "OPEN" if is_open else "CLOSED"
    return status

if __name__ == "__main__":
    status = get_market_status()
    print("🌐 Global Market Status:")
    for k, v in status.items():
        print(f" - {k}: {v}")
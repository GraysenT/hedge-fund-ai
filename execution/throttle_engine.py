
from datetime import datetime, timedelta

THROTTLE_STATE = {}

def should_throttle(symbol, strategy, min_interval_minutes=5):
    key = f"{symbol}_{strategy}"
    now = datetime.utcnow()
    last_time = THROTTLE_STATE.get(key)

    if last_time and now - last_time < timedelta(minutes=min_interval_minutes):
        return True

    THROTTLE_STATE[key] = now
    return False
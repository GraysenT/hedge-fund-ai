import json
import os
from datetime import datetime

TICK_LOG = "logs/tick_events.json"

def fast_route_from_ticks():
    if not os.path.exists(TICK_LOG):
        return

    with open(TICK_LOG) as f:
        ticks = json.load(f)

    for tick in ticks:
        if tick["volume"] > 900:
            print(f"⚠️ High-volume spike: {tick['asset']} at {tick['price']} — route MARKET BUY")

if __name__ == "__main__":
    fast_route_from_ticks()
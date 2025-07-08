import time
import random

def mock_tick(symbol):
    return {
        "symbol": symbol,
        "timestamp": time.time_ns(),  # nanosecond precision
        "price": round(random.uniform(210, 220), 2)
    }

def simulate(symbols, ticks=5):
    log = []
    for _ in range(ticks):
        for sym in symbols:
            tick = mock_tick(sym)
            recv_time = time.time_ns()
            latency_us = (recv_time - tick["timestamp"]) // 1000
            log.append((sym, tick["price"], latency_us))
            print(f"{sym} @ {tick['price']} | Latency: {latency_us}µs")
            time.sleep(0.001)
    return log

if __name__ == "__main__":
    simulate(["TSLA", "AAPL", "MSFT"])

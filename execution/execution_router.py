import random

def route_order(order):
    asset = order["asset"]
    size = order["size"]
    volatility = order.get("volatility", 0.02)
    liquidity = order.get("liquidity", "high")

    method = "limit" if volatility < 0.015 else "market"
    venue = "primary" if liquidity == "high" else "dark_pool"

    slippage = round(random.uniform(0.01, 0.15) * size, 2)

    return {
        "asset": asset,
        "size": size,
        "method": method,
        "venue": venue,
        "expected_slippage": slippage
    }
import pandas as pd

def rebalance_portfolio(current_allocs, target_allocs, total_value):
    orders = []
    for asset, target_pct in target_allocs.items():
        current_val = current_allocs.get(asset, 0)
        desired_val = total_value * target_pct
        diff = desired_val - current_val
        if abs(diff) / total_value > 0.01:
            qty = int(diff // 1)
            orders.append({"symbol": asset, "qty": qty, "side": "buy" if qty > 0 else "sell"})
    return orders
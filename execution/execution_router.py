"""
Handles order execution for all strategies.
Returns execution results with status, side, and simulated pnl.
"""

import random

def route_order(strategy_name, signal):
    """
    Routes a strategy's signal to execution.

    Parameters:
    - strategy_name: str
    - signal: str (e.g. 'buy', 'sell', 'skip')

    Returns:
    - dict with execution result
    """
    if signal == "skip":
        print(f"[EXECUTE] {strategy_name}: Skipped due to signal override.")
        return {
            "status": "skipped"
        }

    print(f"[EXECUTE] {strategy_name}: {signal.upper()} order sent.")

    # Simulated PnL (mock logic — replace with live calc if needed)
    simulated_pnl = round(random.uniform(-1.5, 2.0), 2)  # ±$1.50 to $2.00 profit/loss

    return {
        "status": "executed",
        "side": signal,
        "pnl": simulated_pnl
    }
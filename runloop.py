"""
Main autonomous execution loop for the hedge fund AI system.
- Routes strategies
- Applies patches
- Executes orders
- Logs trades and signals
"""

import time
import json
import os
from execution.strategy_router import route_all_strategies
from execution.execution_router import route_order
from utils.paths import TRADE_LOG_FILE, SIGNAL_LOG
from utils.log_utils import rotate_log
rotate_log(TRADE_LOG_FILE)
rotate_log(SIGNAL_LOG)

def run_main_cycle():
    print("📈 Starting Hedge Fund AI Main Loop...")

    # Step 1: Route signals
    signals = route_all_strategies()

    # Step 2: Execute each signal
    executed_trades = {}
    for strategy_name, signal in signals.items():
        try:
            result = route_order(strategy_name, signal)
            executed_trades[strategy_name] = result
        except Exception as e:
            print(f"[EXECUTION ERROR] {strategy_name}: {e}")
            executed_trades[strategy_name] = {"status": "error", "error": str(e)}

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Step 3: Log trade execution
    trade_entry = {
        "timestamp": timestamp,
        "signals": signals,
        "executions": executed_trades
    }

    if not os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(TRADE_LOG_FILE, "r") as f:
            trade_log = json.load(f)
            if not isinstance(trade_log, list):
                print("⚠️ trade_log.json was not a list. Resetting.")
                trade_log = []
    except json.JSONDecodeError:
        print("⚠️ trade_log.json was corrupted. Resetting.")
        trade_log = []

    trade_log.append(trade_entry)

    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(trade_log, f, indent=2)

    # Step 4: Log raw signals for history tracking
    signal_entry = {
        "timestamp": timestamp,
        "signals": signals
    }

    if not os.path.exists(SIGNAL_LOG):
        with open(SIGNAL_LOG, "w") as f:
            json.dump([], f)

    try:
        with open(SIGNAL_LOG, "r") as f:
            signal_log = json.load(f)
            if not isinstance(signal_log, list):
                print("⚠️ signal_log.json was not a list. Resetting.")
                signal_log = []
    except json.JSONDecodeError:
        print("⚠️ signal_log.json was corrupted. Resetting.")
        signal_log = []

    signal_log.append(signal_entry)

    with open(SIGNAL_LOG, "w") as f:
        json.dump(signal_log, f, indent=2)

    print("✅ Cycle complete.\n")

if __name__ == "__main__":
    while True:
        run_main_cycle()
        time.sleep(1)  # Run once per second
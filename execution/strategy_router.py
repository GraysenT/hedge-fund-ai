
"""
Routes all active strategies, skips muted ones, applies patches,
and collects signals for execution.
"""

import os
import importlib
from alerts.strategy_triggers import load_muted_strategies
from risk_control.patch_slow_react_scalper import patch_slow_react_scalper

# Auto-apply patches
patch_slow_react_scalper()

# Strategy directory path
STRATEGY_DIR = "strategies"

def discover_strategies():
    """Dynamically discover all .py strategy files (excluding __init__)"""
    strategies = []
    for fname in os.listdir(STRATEGY_DIR):
        if fname.endswith(".py") and not fname.startswith("__"):
            strategies.append(fname.replace(".py", ""))
    return strategies

def run_strategy(strategy_name):
    """Safely load and execute the strategy's generate_signal function."""
    try:
        module = importlib.import_module(f"strategies.{strategy_name}")
        if hasattr(module, "generate_signal"):
            signal = module.generate_signal()
            print(f"[ROUTER] {strategy_name}: {signal}")
            return strategy_name, signal
        else:
            print(f"[ROUTER] {strategy_name} has no generate_signal()")
    except Exception as e:
        print(f"[ROUTER ERROR] {strategy_name} failed: {e}")
    return strategy_name, None

def route_all_strategies():
    """Main router loop."""
    muted = load_muted_strategies()
    signals = {}

    for strategy_name in discover_strategies():
        if strategy_name in muted:
            print(f"[ROUTER] Skipping muted strategy: {strategy_name}")
            continue

        name, signal = run_strategy(strategy_name)
        if signal:
            signals[name] = signal

    return signals

if __name__ == "__main__":
    signals = route_all_strategies()
    print("\n[ROUTER] Final Signals:", signals)
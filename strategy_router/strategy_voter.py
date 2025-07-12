"""
Strategy Voting Engine: Allows strategies to self-score or vote based on performance.
This version returns all active strategies that haven't been muted.
"""

import os
from alerts.strategy_triggers import load_muted_strategies
from execution.strategy_router import discover_strategies

def run_strategy_voting():
    """
    Returns a list of strategies that are allowed to proceed to deployment filtering.
    Currently allows all strategies that are not muted.
    """
    muted = load_muted_strategies()
    strategies = discover_strategies()

    approved = [s for s in strategies if s not in muted]
    print(f"[VOTER] Approved strategies after voting: {approved}")
    return approved
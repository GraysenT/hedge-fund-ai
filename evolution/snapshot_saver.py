import os
import pandas as pd
from datetime import datetime
from pathlib import Path

from portfolio_ai.full_allocator import load_allocation_snapshot
from alerts.strategy_triggers import (
    load_muted_strategies_df,
    load_rewarded_strategies_df,
)

SNAPSHOT_DIR = Path("snapshots")
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

def save_evolution_snapshot():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    folder = SNAPSHOT_DIR / f"snapshot_{timestamp}"
    folder.mkdir(parents=True, exist_ok=True)

    # Save current strategy allocations
    alloc_df = load_allocation_snapshot()
    if not alloc_df.empty:
        alloc_df.to_csv(folder / "allocations.csv", index=False)

    # Save muted strategies
    muted_df = load_muted_strategies_df()
    if not muted_df.empty:
        muted_df.to_csv(folder / "muted_strategies.csv", index=False)

    # Save rewarded strategies
    rewarded_df = load_rewarded_strategies_df()
    if not rewarded_df.empty:
        rewarded_df.to_csv(folder / "rewarded_strategies.csv", index=False)

    print(f"📸 Evolution snapshot saved to {folder.resolve()}")
    
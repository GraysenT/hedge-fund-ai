import pandas as pd
from pathlib import Path

CLASSIFIED_PATH = Path("classified_failures/classified_signal_failures.csv")
PATTERN_PATH = Path("memory/pattern_memory.csv")

def update_pattern_memory():
    if not CLASSIFIED_PATH.exists():
        print("🚫 No classified signal failures to process.")
        return

    df = pd.read_csv(CLASSIFIED_PATH)
    if df.empty:
        return

    # Classify fragility
    grouped = df.groupby("strategy")
    memory = []
    for strat, sub in grouped:
        total = len(sub)
        fails = sub[sub["failure"] == True]
        fragility_rate = round(len(fails) / total, 4)

        # Anti-fragile detection: do they bounce back after a loss?
        anti_fragile_hits = 0
        sorted_sub = sub.sort_values("date")
        for i in range(1, len(sorted_sub)):
            prev = sorted_sub.iloc[i - 1]
            curr = sorted_sub.iloc[i]
            if prev["failure"] and not curr["failure"]:
                anti_fragile_hits += 1

        memory.append({
            "strategy": strat,
            "fragility_rate": fragility_rate,
            "anti_fragile_bounces": anti_fragile_hits,
            "total_signals": total
        })

    mem_df = pd.DataFrame(memory)
    mem_df.to_csv(PATTERN_PATH, index=False)
    print(f"🧠 Pattern memory updated: {PATTERN_PATH}")

def load_pattern_memory():
    if PATTERN_PATH.exists():
        return pd.read_csv(PATTERN_PATH)
    return pd.DataFrame()
    
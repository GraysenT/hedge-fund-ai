import pandas as pd
from utils.paths import STRATEGY_STATUS_FILE

def apply_alpha_defense(min_health_threshold=0.1):
    try:
        df = pd.read_json(STRATEGY_STATUS_FILE)
    except Exception as e:
        print(f"[AlphaDefense] Failed to load status: {e}")
        return []

    muted = []
    for i, row in df.iterrows():
        if row.get("AlphaHealth", 1.0) < min_health_threshold:
            df.at[i, "Muted"] = True
            muted.append(row["Strategy"])
        else:
            df.at[i, "Muted"] = False

    df.to_json(STRATEGY_STATUS_FILE, indent=2)
    print(f"[AlphaDefense] Muted {len(muted)} decaying strategies.")
    return muted
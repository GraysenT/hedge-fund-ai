import os
import json
from datetime import datetime
from reinforcement.survival_tracker import load_snapshots, score_survival

LOG_DIR = "strategy_memory/evolution_logs"

def log_daily_evolution():
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(LOG_DIR, f"evolution_log_{timestamp}.json")

    snapshots = load_snapshots()
    df = score_survival(snapshots)

    muted = df[df["Status"] == "🔽 Decaying"]["Strategy"].tolist()
    promoted = df[df["Status"] == "🔼 Promising"]["Strategy"].tolist()

    log = {
        "timestamp": timestamp,
        "muted_strategies": muted,
        "promoted_strategies": promoted,
        "summary": df.to_dict(orient="records")
    }

    with open(log_path, 'w') as f:
        json.dump(log, f, indent=2)

    print(f"✅ Daily evolution log saved to {log_path}")
    print(f"🔇 Muted: {len(muted)} | 🚀 Promoted: {len(promoted)}")

if __name__ == '__main__':
    log_daily_evolution()

import os
import shutil
import datetime


def run():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    target_dir = os.path.join("logs", "history", today)

    os.makedirs(target_dir, exist_ok=True)

    files_to_copy = [
        "strategy_weights.csv",
        "strategy_weights_decayed.csv",
        "strategy_weights_reinforced.csv",
        "strategy_routing.csv",
        "portfolio_memory.csv",
        "muted_strategies.csv",
        "strategy_promotions.csv"
    ]

    copied = []
    for fname in files_to_copy:
        src = os.path.join("logs", fname)
        if os.path.exists(src):
            dst = os.path.join(target_dir, fname)
            shutil.copy(src, dst)
            copied.append(fname)

    print(f"📘 Snapshot for {today} saved.")
    print("🗃 Files archived:")
    for f in copied:
        print(f" → {f}")


if __name__ == "__main__":
    run()

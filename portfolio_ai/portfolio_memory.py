import pandas as pd
import os
import datetime


def run():
    print("\n🧠 Portfolio Memory Tracker Running...")

    weights_path = os.path.join("logs", "strategy_weights.csv")
    memory_path = os.path.join("logs", "portfolio_memory.csv")

    if not os.path.exists(weights_path):
        print("🚫 No strategy weights found.")
        return

    df = pd.read_csv(weights_path)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    df["Date"] = today

    # Append to memory file
    file_exists = os.path.isfile(memory_path)
    with open(memory_path, mode="a", newline="") as f:
        df.to_csv(f, header=not file_exists, index=False)

    print(f"📘 Daily portfolio snapshot saved to {memory_path}")


if __name__ == "__main__":
    run()

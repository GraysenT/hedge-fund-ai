import os
import json
import pandas as pd

folder = "memory/order_logs"
if not os.path.exists(folder):
    print("❌ No order logs found.")
    exit()

latest = sorted(os.listdir(folder))[-1]
with open(os.path.join(folder, latest)) as f:
    orders = json.load(f)

df = pd.DataFrame(orders)

if df.empty:
    print(f"⚠️ Order log {latest} is empty.")
else:
    print(f"\n📋 Live Order Log — {latest}:\n")
    print(df[["timestamp", "strategy", "symbol", "action", "qty", "price"]].to_string(index=False))
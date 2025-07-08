import pandas as pd
import os
from datetime import datetime, timedelta
import random

symbols = ["AAPL", "TSLA", "MSFT"]
now = datetime.now()

os.makedirs("data/price_history", exist_ok=True)

for symbol in symbols:
    rows = []
    for i in range(10):
        ts = (now - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
        price = round(100 + random.uniform(-5, 5), 2)
        rows.append({"timestamp": ts, "close": price})

    df = pd.DataFrame(rows)
    df.to_csv(f"data/price_history/{symbol}.csv", index=False)

print("✅ Mock price history created for:", symbols)

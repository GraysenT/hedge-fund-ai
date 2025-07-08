from pathlib import Path
import pandas as pd
from datetime import datetime

def log_account_trade(account_id: str, trade_data: dict):
    folder = Path(f"execution_logs/{account_id}")
    folder.mkdir(parents=True, exist_ok=True)

    today = datetime.utcnow().strftime("%Y-%m-%d")
    path = folder / f"trades_{today}.csv"

    df = pd.DataFrame([trade_data])
    if path.exists():
        df.to_csv(path, mode="a", index=False, header=False)
    else:
        df.to_csv(path, index=False)

    print(f"✅ Trade logged for {account_id}")
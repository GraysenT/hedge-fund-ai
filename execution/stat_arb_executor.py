import pandas as pd
from datetime import datetime
from pathlib import Path

TRADE_LOG = Path("execution_logs/stat_arb_trades.csv")
TRADE_LOG.parent.mkdir(parents=True, exist_ok=True)

def execute_stat_arb_signals(signals_df):
    executed = []

    for _, row in signals_df.iterrows():
        order = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "pair": row["pair"],
            "t1": row["t1"],
            "t2": row["t2"],
            "side_t1": "buy" if "long" in row["signal"] and "t1" in row["signal"] else "sell",
            "side_t2": "sell" if "short" in row["signal"] and "t2" in row["signal"] else "buy",
            "zscore": row["zscore"],
            "confidence": row["confidence"],
            "spread": row["spread"]
        }
        executed.append(order)

    if executed:
        df = pd.DataFrame(executed)
        if TRADE_LOG.exists():
            df.to_csv(TRADE_LOG, mode='a', index=False, header=False)
        else:
            df.to_csv(TRADE_LOG, index=False)

        print(f"✅ Executed {len(df)} stat arb trades.")
    else:
        print("🟡 No stat arb trades executed.")
        
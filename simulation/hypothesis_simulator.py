import pandas as pd
from datetime import datetime
from pathlib import Path

PROMOTED_PATH = Path("memory/promoted_hypotheses.csv")
SIM_LOG_PATH = Path("simulation/hypothesis_sim_log.csv")
SIGNAL_PATH = Path("signal_logs")

def run_simulation():
    if not PROMOTED_PATH.exists():
        print("🛑 No promoted hypotheses found.")
        return

    promoted_df = pd.read_csv(PROMOTED_PATH)
    if promoted_df.empty:
        print("🟡 Promoted hypothesis list is empty.")
        return

    types = promoted_df["promoted_types"].tolist()
    signal_files = list(SIGNAL_PATH.glob("signals_*.csv"))

    results = []
    for f in signal_files:
        df = pd.read_csv(f)
        for strategy_type in types:
            matching = df[df["strategy"].str.contains(strategy_type, case=False, na=False)]
            for _, row in matching.iterrows():
                result = {
                    "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    "strategy": row["strategy"],
                    "confidence": row.get("confidence", 0.5),
                    "signal": row["signal"],
                    "ticker": row.get("ticker", ""),
                    "source": f.name
                }
                results.append(result)

    if results:
        sim_df = pd.DataFrame(results)
        if SIM_LOG_PATH.exists():
            sim_df.to_csv(SIM_LOG_PATH, mode="a", header=False, index=False)
        else:
            sim_df.to_csv(SIM_LOG_PATH, index=False)
        print(f"✅ Simulated {len(sim_df)} hypothesis signals.")
    else:
        print("🟡 No matching signals found for promoted ideas.")
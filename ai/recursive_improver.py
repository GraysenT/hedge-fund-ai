import pandas as pd
from datetime import datetime
from pathlib import Path

HYP_RESULTS = Path("memory/hypothesis_results.csv")
PROMOTED_PATH = Path("memory/promoted_hypotheses.csv")

def promote_successful_hypotheses(min_pass_rate=0.8):
    df = pd.read_csv(HYP_RESULTS)
    df["type"] = df["idea"].apply(lambda x: x.split()[0])
    group = df.groupby("type")["result"].apply(lambda x: (x == "pass").mean())

    promoted = group[group >= min_pass_rate].index.tolist()

    output = pd.DataFrame({
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "promoted_types": promoted
    })

    output.to_csv(PROMOTED_PATH, index=False)
    print(f"🚀 Promoted hypothesis types: {promoted}")
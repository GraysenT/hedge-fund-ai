import pandas as pd
from pathlib import Path
from datetime import datetime

HYPOTHESIS_PATH = Path("memory/research_hypotheses.csv")

def generate_new_hypotheses():
    ideas = [
        "Use PCA to reduce strategy correlation before optimization",
        "Introduce macro regime tag for all signals",
        "Tag spike-reversal patterns in volatility engine",
        "Apply adaptive learning rate in reinforcement engine"
    ]

    df = pd.DataFrame({
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "idea": ideas
    })

    if HYPOTHESIS_PATH.exists():
        df.to_csv(HYPOTHESIS_PATH, mode="a", header=False, index=False)
    else:
        df.to_csv(HYPOTHESIS_PATH, index=False)

    print("🧠 New hypotheses generated.")
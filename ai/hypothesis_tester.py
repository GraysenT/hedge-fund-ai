import pandas as pd
from datetime import datetime
from pathlib import Path

HYPOTHESIS_PATH = Path("memory/research_hypotheses.csv")
RESULTS_PATH = Path("memory/hypothesis_results.csv")

def test_hypotheses():
    if not HYPOTHESIS_PATH.exists():
        print("🛑 No hypotheses to test.")
        return

    df = pd.read_csv(HYPOTHESIS_PATH)
    tested = []

    for _, row in df.iterrows():
        idea = row["idea"]
        result = "pass" if "PCA" in idea or "volatility" in idea else "fail"
        tested.append({
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "idea": idea,
            "result": result
        })

    pd.DataFrame(tested).to_csv(RESULTS_PATH, index=False)
    print(f"🧪 Hypotheses tested: {RESULTS_PATH}")
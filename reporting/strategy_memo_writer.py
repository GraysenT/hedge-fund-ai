import openai
import json
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
LINEAGE = "strategy_memory/strategy_lineage.json"

def write_memos():
    lineage = json.load(open(LINEAGE))
    selected = list(lineage.keys())[-5:]

    for strat in selected:
        info = lineage[strat]
        prompt = f"""
You're a quant researcher. Write a 1-page research memo explaining this strategy:

Name: {strat}
Depth: {info.get('depth')}
Model: {info.get('model')}
Rating: {info.get('rating')}
Parent: {info.get('parent')}

Describe logic, market behavior it exploits, strengths, and risks.
"""

        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        memo = res["choices"][0]["message"]["content"]
        path = f"reporting/strategy_memos/{strat}_memo.txt"
        os.makedirs("reporting/strategy_memos", exist_ok=True)
        with open(path, "w") as f:
            f.write(memo)
        print(f"🧾 Memo saved: {path}")

if __name__ == "__main__":
    write_memos()
    
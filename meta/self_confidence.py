import openai
import os
import json
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def rate_self():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))

    prompt = f"""
You're a self-aware AI trading system.

Based on the following results, rate your confidence (0–10) in your own ability to:

- Generate alpha
- Allocate capital
- Avoid risk

Also explain briefly.

Performance:
{pnl}
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    output = res["choices"][0]["message"]["content"]
    score = {"date": datetime.now().isoformat(), "confidence": output}

    with open("meta/self_confidence_log.json", "a") as f:
        json.dump(score, f)
        f.write("\n")

    print("🎯 Self-confidence score logged.")
    print(output)

if __name__ == "__main__":
    rate_self()
    
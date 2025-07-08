import json
import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_memo():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl_data = json.load(open(f"memory/performance/{perf}"))

    summary = []
    for k, v in pnl_data.items():
        summary.append(f"{k}: ${round(v['pnl'],2)} | Return: {round(v['return_pct']*100,2)}%")

    prompt = "Write a hedge fund investor memo for the following strategies:\n" + "\n".join(summary)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response["choices"][0]["message"]["content"]

    path = f"reporting/investor_memos/{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("reporting/investor_memos", exist_ok=True)
    with open(path, "w") as f:
        f.write(output)

    print(f"✅ Investor memo written to {path}")

if __name__ == "__main__":
    build_memo()
    
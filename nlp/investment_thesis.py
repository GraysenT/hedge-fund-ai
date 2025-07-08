import openai
import json
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_thesis():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))

    prompt = f"""
You're the head of research for an AI hedge fund.

Given the following recent strategy performance:
{pnl}

Write an investment thesis in 3–5 bullet points:
- Focus areas
- Themes
- Risk signals
- Style shifts
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    thesis = response["choices"][0]["message"]["content"]
    path = f"meta/thesis_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(path, "w") as f:
        f.write(thesis)

    print(f"📖 Thesis written to {path}")
    return thesis

if __name__ == "__main__":
    generate_thesis()

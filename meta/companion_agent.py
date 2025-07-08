import openai
import os
import json
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def observe():
    perf = json.load(open("memory/performance/" + sorted(os.listdir("memory/performance"))[-1]))
    firewall = json.load(open("meta/alpha_firewall.json")) if os.path.exists("meta/alpha_firewall.json") else []

    prompt = f"""
You're the live companion AI for a trading system.

Today’s performance:
{perf}

Firewalled strategies:
{firewall}

Based on this, provide:
- 2 observations
- 1 concern
- 1 opportunity
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    text = res["choices"][0]["message"]["content"]
    path = f"meta/companion_logs/log_{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("meta/companion_logs", exist_ok=True)
    with open(path, "w") as f:
        f.write(text)

    print(f"🧑‍💻 Companion agent report written to {path}")
    print(text)

if __name__ == "__main__":
    observe()
    
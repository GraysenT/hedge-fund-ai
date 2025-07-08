import openai
import os
import json
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_context():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))

    audit = sorted(os.listdir("reporting/audits"))[-1]
    audit_txt = open(f"reporting/audits/{audit}").read()

    return pnl, audit_txt

def reflect():
    pnl, audit = get_context()
    prompt = f"""
You are an autonomous trading AI reflecting on today.

Here's your performance:\n{pnl}
Audit findings:\n{audit}

Please write a 5-point reflection:
1. What did I do well?
2. What did I do poorly?
3. What patterns did I observe?
4. What should I try tomorrow?
5. One thing to remember.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    reflection = response["choices"][0]["message"]["content"]

    path = f"meta/reflections/reflection_{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("meta/reflections", exist_ok=True)
    with open(path, "w") as f:
        f.write(reflection)

    print(f"🧠 Reflection written to: {path}")
    print(reflection)

if __name__ == "__main__":
    reflect()
    
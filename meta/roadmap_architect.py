import openai
import json
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
DEV_LOG = "meta/dev_log.json"

def generate_roadmap():
    log = json.load(open(DEV_LOG))
    recent = sorted(log, key=lambda x: x["date"], reverse=True)[:5]

    prompt = f"""
You're the AI architect of a self-evolving hedge fund OS.

Based on recent upgrades:\n{recent}

Propose 3–5 intelligent next-phase upgrades with rationale.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    plan = response["choices"][0]["message"]["content"]
    path = f"meta/roadmaps/roadmap_AI_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(path, "w") as f:
        f.write(plan)
    print(f"🗺 AI roadmap architect wrote plan to: {path}")
    print(plan)

if __name__ == "__main__":
    generate_roadmap()
    
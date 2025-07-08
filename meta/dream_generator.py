import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def dream():
    prompt = """
You're an AI hedge fund dreaming overnight.

Based on recent strategies and performance, invent a new strategy idea. Describe:
- Market setup
- Indicators
- Timeframe
- Expected edge

Write it like a journal note from a dream.
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    content = res["choices"][0]["message"]["content"]
    path = f"meta/dreams/dream_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt"
    os.makedirs("meta/dreams", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

    print(f"💭 Dream saved: {path}")
    print(content)

if __name__ == "__main__":
    dream()
    
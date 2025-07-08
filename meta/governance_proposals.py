import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def propose_upgrade():
    prompt = """
You are the internal architect of an AI hedge fund.

Propose one new system upgrade or feature that:
- Improves alpha, performance, or stability
- Can be implemented in the next 48 hours
- Has a clear title and rationale

Return as:
- Title
- Description
- Implementation Outline
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    content = res["choices"][0]["message"]["content"]
    path = f"meta/proposals/proposal_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt"
    os.makedirs("meta/proposals", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

    print(f"📜 Proposal written to: {path}")
    print(content)

if __name__ == "__main__":
    propose_upgrade()
    
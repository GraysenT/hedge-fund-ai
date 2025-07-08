import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_peer(file_path):
    with open(file_path, "r") as f:
        bundle = json.load(f)

    prompt = f"""
You are an AI portfolio strategist.

Given this peer fund's strategy data and recent performance, summarize:
- Dominant trading styles
- Market assumptions
- Strengths
- Blind spots
- Fusion opportunities

Bundle:
{bundle}
"""

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print("📖 Peer Fund Summary:\n")
    print(res["choices"][0]["message"]["content"])

if __name__ == "__main__":
    peer_file = sorted(f for f in os.listdir("federation") if "import" in f)[-1]
    summarize_peer(f"federation/{peer_file}")
    
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_roadmap():
    prompt = """
You're the long-term planning AI for a hedge fund system.

You must output:
- 3-day short-term optimization tasks
- 3-week model, strategy, or data upgrades
- 3-month scaling and evolution roadmap

Include alpha objectives, priorities, and rationale.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    plan = response["choices"][0]["message"]["content"]
    path = f"meta/roadmaps/roadmap_{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("meta/roadmaps", exist_ok=True)
    with open(path, "w") as f:
        f.write(plan)

    print(f"🧭 Roadmap saved to {path}")

if __name__ == "__main__":
    generate_roadmap()
    
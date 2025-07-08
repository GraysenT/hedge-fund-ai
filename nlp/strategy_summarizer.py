import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_strategy(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    prompt = f"""
You're a professional quant research analyst. Explain in 3–4 sentences what this strategy does.

Python code:
{code}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    summary = summarize_strategy("plugins/sample_strategy.py")
    print("📝 Summary:\n", summary)
    
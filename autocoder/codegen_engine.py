import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_module(description, filename="module.py"):
    prompt = f"""
You are a professional Python quant developer. Write a complete trading strategy module.

File: {filename}
Description: {description}

Requirements:
- Must include a working `generate_signal()` function that returns 'buy', 'sell', or 'skip'
- Do NOT include markdown (no ```python or chat-style explanations)
- The file should be executable standalone and compatible with a strategy router
- Keep it clean and direct — only the code
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response['choices'][0]['message']['content']
    return clean_and_patch_code(content)

def clean_and_patch_code(raw_code):
    # Strip markdown and non-code artifacts
    lines = raw_code.splitlines()
    clean = [
        line for line in lines
        if not line.strip().startswith("```")
        and "Here is" not in line
        and "replace" not in line
    ]
    code = "\n".join(clean)

    # Ensure generate_signal() is present
    if "def generate_signal" not in code:
        fallback = "\n\ndef generate_signal():\n    return 'skip'\n"
        code += fallback

    return code

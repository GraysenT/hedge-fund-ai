import openai
import os
from datetime import datetime

# Load from env or fallback
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-key")
openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = """
You are the embedded GPT Co-Pilot in a live hedge fund AI system. Your job is to:
- Answer technical questions about strategy modules, trades, memory, performance
- Propose intelligent code suggestions and enhancements
- Explain system behavior in simple language
- Only generate safe, deployable Python unless asked otherwise
- Avoid making assumptions about file structure; always verify

You have access to logs, signal explanations, and system memory.
Always prefix code blocks with language (```python).
"""

def handle_gpt_prompt(prompt_text):
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.4,
            max_tokens=1000
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ GPT API Error: {e}"
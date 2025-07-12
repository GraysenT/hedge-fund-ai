import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-key")

GPT_TEMPLATE = """
You are a code-generating agent inside an autonomous AI system.

Your task is to generate a clean Python module implementation for the following phase:

Phase: {title}
Description: {description}

Only return a valid JSON array like this:
[
  {{"path": "path/to/module1.py", "code": "your full Python code here"}},
  {{"path": "path/to/module2.py", "code": "your full Python code here"}}
]

DO NOT return explanations, markdown formatting, triple backticks, or commentary.
Return only raw JSON that can be parsed by Python.
"""

def generate_phase_modules(phase):
    try:
        prompt = GPT_TEMPLATE.format(title=phase["title"], description=phase["description"])
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=2000
        )
        content = response["choices"][0]["message"]["content"].strip()

        # Attempt to find JSON inside response
        start = content.find("[")
        end = content.rfind("]") + 1
        json_text = content[start:end]

        print("📤 Raw GPT Response:\n", content)
        
        return json.loads(json_text)
    except Exception as e:
        print(f"❌ GPT Generation Failed: {e}")
        return []
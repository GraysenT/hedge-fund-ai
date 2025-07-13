import openai
import os
import json

class GPTReasoningEngine:
    def __init__(self, api_key=None):
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def ask(self, prompt: str, context: dict = None) -> str:
        messages = [{"role": "system", "content": "You are the mind of the hedge fund AI."}]
        if context:
            context_text = json.dumps(context, indent=2)
            messages.append({"role": "system", "content": f"Here is your memory: {context_text}"})
        messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        return response.choices[0].message.content.strip()
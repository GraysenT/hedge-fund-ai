from openai import OpenAI
import os

def ask_intelligence(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are the hedge fund brain. Explain yourself."},
                  {"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
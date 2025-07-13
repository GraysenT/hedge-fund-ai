import openai
import os

class InnerDialogue:
    def __init__(self, agent_name):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.agent_name = agent_name
        self.dialogue = []

    def think(self, question):
        prompt = f"{self.agent_name} internal thoughts:\n" + "\n".join(self.dialogue[-3:]) + f"\nQ: {question}\nA:"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are the inner voice of an AI agent optimizing trading."},
                      {"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        self.dialogue.append(f"Q: {question}\nA: {answer}")
        return answer
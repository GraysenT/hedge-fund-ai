import openai
import datetime

def generate_strategy_code(prompt: str, model="gpt-4"):
    """
    Uses LLM prompting to generate valid strategy code from natural language ideas.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": "Write a new alpha strategy in Python."},
                      {"role": "user", "content": prompt}]
        )
        code = response['choices'][0]['message']['content']
        timestamp = datetime.datetime.utcnow().isoformat()
        return {"code": code, "created": timestamp}
    except Exception as e:
        return {"error": str(e)}
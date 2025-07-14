import subprocess

def ask_oracle(context: str, question: str = "How can this be improved?"):
    prompt = f"Context: {context}\nQuestion: {question}"
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode().strip()
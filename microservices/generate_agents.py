import os

AGENT_NAMES = [
    "strategy", "macro", "sentiment", "risk"
] + [f"gen{i}" for i in range(1, 250)]  # Extendable to 273

DOCKERFILE_TEMPLATE = '''
FROM baseimage:latest
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
'''

for agent in AGENT_NAMES:
    path = f"services/agent_{agent}"
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/Dockerfile", "w") as f:
        f.write(DOCKERFILE_TEMPLATE)
    print(f"Dockerfile updated for agent: agent_{agent}")
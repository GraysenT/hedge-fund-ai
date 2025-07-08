import json
import random
from datetime import datetime

MODELS = ["LSTM", "CNN", "Transformer"]
SCORES_FILE = "models/model_scores.json"

def simulate_model_return(model_type):
    return round(random.uniform(-0.01, 0.03), 4)

def update_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE) as f:
            scores = json.load(f)
    else:
        scores = {}

    for m in MODELS:
        score = simulate_model_return(m)
        scores[m] = scores.get(m, 0) * 0.9 + score
        print(f"🔄 {m} → new reward: {score:.4f}, total: {scores[m]:.4f}")

    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def pick_best():
    with open(SCORES_FILE) as f:
        scores = json.load(f)
    return max(scores, key=scores.get)

if __name__ == "__main__":
    update_scores()
    best = pick_best()
    print(f"🏆 Selected model for next run: {best}")

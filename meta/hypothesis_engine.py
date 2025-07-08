import uuid
import json
import os
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RESEARCH_DB = "memory/research_memory.json"
os.makedirs("memory", exist_ok=True)

def load_memory():
    if os.path.exists(RESEARCH_DB):
        with open(RESEARCH_DB, "r") as f:
            return json.load(f)
    return []

def save_memory(memory):
    with open(RESEARCH_DB, "w") as f:
        json.dump(memory, f, indent=2)

def generate_hypothesis(idea, supporting_context, simulation_score):
    memory = load_memory()
    entry_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    new_entry = {
        "id": entry_id,
        "idea": idea,
        "context": supporting_context,
        "score": simulation_score,
        "timestamp": timestamp
    }

    memory.append(new_entry)
    save_memory(memory)
    print(f"💡 New hypothesis saved: {idea[:80]}...")

def find_similar_hypotheses(query):
    memory = load_memory()
    documents = [m["idea"] for m in memory]
    if not documents:
        return []

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents + [query])
    scores = cosine_similarity(vectors[-1:], vectors[:-1])[0]
    ranked = sorted(zip(memory, scores), key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked[:5] if r[1] > 0.3]

# Example manual test
if __name__ == "__main__":
    generate_hypothesis(
        idea="MACD divergence near Fed meeting boosts intraday reversal likelihood",
        supporting_context="Used on SPY and QQQ during FOMC events, MACD + RSI + volume triggers.",
        simulation_score=0.82
    )

    matches = find_similar_hypotheses("momentum reversal around macro events")
    for m in matches:
        print(f"🔍 Similar: {m['idea']} | Score: {m['score']}")
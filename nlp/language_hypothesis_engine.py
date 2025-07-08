import uuid
import json
import os
from datetime import datetime
from transformers import pipeline

hypothesis_log = "memory/language_hypotheses.json"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def generate_hypotheses_from_headlines(headlines):
    os.makedirs("memory", exist_ok=True)
    memory = []
    for hl in headlines:
        summary = summarizer(hl, max_length=30, min_length=5, do_sample=False)[0]["summary_text"]
        idea = f"If {summary.lower()}, then expect macro reversal or breakout."

        memory.append({
            "id": str(uuid.uuid4()),
            "idea": idea,
            "source": hl,
            "timestamp": datetime.utcnow().isoformat()
        })

    with open(hypothesis_log, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"📰 Generated {len(memory)} language-based hypotheses.")
    return memory

if __name__ == "__main__":
    sample_headlines = [
        "Fed signals potential rate cut amid slowing inflation",
        "Apple launches new AI chip for mobile trading apps",
        "Oil surges after Middle East supply disruption"
    ]
    generate_hypotheses_from_headlines(sample_headlines)
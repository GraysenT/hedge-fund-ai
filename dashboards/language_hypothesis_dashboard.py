import json
import os

def show_language_hypothesis_dashboard():
    path = "memory/language_hypotheses.json"
    if not os.path.exists(path):
        print("❌ No NLP hypotheses found.")
        return

    with open(path) as f:
        data = json.load(f)

    print("\n🧠 Language-Aware Alpha Ideas:")
    for d in data[:5]:
        print(f"- {d['idea']} (source: {d['source'][:40]}...)")

if __name__ == "__main__":
    show_language_hypothesis_dashboard()
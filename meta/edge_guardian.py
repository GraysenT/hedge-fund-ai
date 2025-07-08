import os
import difflib

PLUGIN_DIR = "plugins"
MEMORY_FILE = "meta/edge_guardian_memory.json"

def compare_plugins():
    files = [f for f in os.listdir(PLUGIN_DIR) if f.endswith(".py")]
    similarities = {}

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            with open(f"{PLUGIN_DIR}/{files[i]}") as f1, open(f"{PLUGIN_DIR}/{files[j]}") as f2:
                text1 = f1.read()
                text2 = f2.read()
                ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
                if ratio > 0.85:
                    similarities[f"{files[i]} vs {files[j]}"] = round(ratio, 4)

    print("🛡 Edge Guardian Similarity Alerts:")
    for pair, score in similarities.items():
        print(f"⚠️ {pair}: {score}")

    with open(MEMORY_FILE, "w") as f:
        import json
        json.dump(similarities, f, indent=2)

if __name__ == "__main__":
    compare_plugins()
    
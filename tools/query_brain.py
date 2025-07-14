import json

with open("logs/brain.jsonl") as f:
    entries = [json.loads(line) for line in f]

while True:
    q = input("Ask your brain > ").lower()
    
    if "dream" in q:
        tick = int(q.split("tick")[-1].strip())
        match = next((e for e in entries if e["tick"] == tick), None)
        print(match["dream"] if match else "❌ Not found.")

    elif "best in crypto" in q:
        best = max(entries, key=lambda e: e['dream'].get("future_price", 0))
        print("🧠 Top crypto dream:", best['dream'])

    elif "oracle said" in q:
        for e in entries[-5:]:
            print(f"Tick {e['tick']}: {e['oracle']}")

    elif q in ["exit", "quit"]:
        break
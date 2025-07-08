import pandas as pd
import os
from datetime import datetime
import hashlib

def generate_id(row):
    string = f"{row['Asset']}_{row['Signal']}_{row['Confidence Range']}_{row['Strategy']}"
    return hashlib.md5(string.encode()).hexdigest()[:8]

def run():
    print("\n🧠 Research Memory Engine Running...")

    new_ideas_path = "logs/generated_hypotheses.csv"
    memory_path = "logs/research_memory.csv"

    if not os.path.exists(new_ideas_path):
        print("❌ No new hypotheses found.")
        return

    new = pd.read_csv(new_ideas_path)
    if new.empty:
        print("ℹ️ No new ideas to log.")
        return

    # Add metadata
    new["Hypothesis ID"] = new.apply(generate_id, axis=1)
    new["Timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Load existing memory
    if os.path.exists(memory_path):
        memory = pd.read_csv(memory_path)
        combined = pd.concat([memory, new]).drop_duplicates(subset=["Hypothesis ID"])
    else:
        combined = new

    # Count recurrence
    freq = combined.groupby("Hypothesis ID").size().reset_index(name="Occurrences")
    combined = combined.merge(freq, on="Hypothesis ID", how="left")

    # Save
    combined.to_csv(memory_path, index=False)
    print(f"✅ Research memory updated: {len(combined)} total hypotheses")

if __name__ == "__main__":
    run()
    
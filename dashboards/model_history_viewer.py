import json
import os
import pandas as pd

metadata_path = "models/model_versions.json"

if not os.path.exists(metadata_path):
    print("❌ No model metadata found.")
    exit()

with open(metadata_path, "r") as f:
    data = json.load(f)

df = pd.DataFrame([
    {
        "Symbol": k,
        "Last Trained": v["last_trained"],
        "Model Path": v["model_path"]
    } for k, v in data.items()
])

df = df.sort_values(by="Last Trained", ascending=False)
print("\n📊 Model Retraining History:\n")
print(df.to_string(index=False))

import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="📊 Final Strategy Weights", layout="wide")
st.title("📊 Final Live Strategy Weights")

BASE_PATH = "strategy_memory/base_weights.json"
REINFORCE_PATH = "strategy_memory/latest_weights.json"

# Load weights safely

def load_weights(path):
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.warning(f"⚠️ File {path} is not valid JSON. Please fix or regenerate it.")
            return {}
    return {}

base_weights = load_weights(BASE_PATH)
reinforce_weights = load_weights(REINFORCE_PATH)

# Combine into DataFrame
data = []
for strategy, base in base_weights.items():
    reinforce = reinforce_weights.get(strategy, 1.0)
    final = round(base * reinforce, 4)
    status = "🔼 Reinforced" if reinforce > 1 else ("🔽 Decayed" if reinforce < 1 else "➖ Neutral")
    data.append({
        "Strategy": strategy,
        "Base Weight": base,
        "Reinforce Multiplier": reinforce,
        "Final Weight": final,
        "Status": status
    })

if data:
    df = pd.DataFrame(data).sort_values(by="Final Weight", ascending=False)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Strategy")["Final Weight"])
else:
    st.warning("⚠️ No strategy weight data found. Please run reinforcement and base allocator first.")

import os
import json
import pandas as pd
import streamlit as st
from utils.paths import STRATEGY_STATUS_FILE

st.set_page_config(page_title="🧬 Mutated Strategy Tracker", layout="wide")
st.title("🧬 Mutated Strategy Performance")

# Load performance scores
if not os.path.exists(STRATEGY_STATUS_FILE):
    st.warning("Strategy status file not found.")
    st.stop()

with open(STRATEGY_STATUS_FILE, "r") as f:
    scores = json.load(f)

# Filter mutated strategies
mutated_scores = {k: v for k, v in scores.items() if "mutated" in k.lower()}

if not mutated_scores:
    st.info("No mutated strategies found.")
    st.stop()

df = pd.DataFrame.from_dict(mutated_scores, orient="index").reset_index()
df = df.rename(columns={"index": "strategy"})
df = df.sort_values(by="sharpe", ascending=False)

st.dataframe(df, use_container_width=True)
st.bar_chart(df.set_index("strategy")["sharpe"])
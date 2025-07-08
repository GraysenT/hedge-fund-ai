import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Self-Learning Patterns", layout="wide")
st.title("🧠 Self-Learning Pattern Tracker")

def load_csv(path):
    return pd.read_csv(path) if os.path.exists(path) else None

# === 1. Self-Labeled Patterns ===
st.subheader("📊 Self-Labeled Successful Patterns")

label_df = load_csv("logs/self_labeled_patterns.csv")
if label_df is not None and not label_df.empty:
    st.dataframe(label_df.sort_values("Success Rate", ascending=False))
    st.caption(f"✅ {len(label_df)} pattern(s) labeled for reinforcement")
else:
    st.warning("⚠️ No self-labeled patterns yet. Run more signals and backtests.")

# === 2. Reinforced Weights (with or without boost) ===
st.divider()
st.subheader("📈 Current Reinforced Strategy Weights")

weights_df = load_csv("logs/strategy_weights_reinforced.csv")
if weights_df is not None:
    st.dataframe(weights_df.round(4))
    st.bar_chart(weights_df.set_index("Strategy")["Reinforced Weight"])
else:
    st.warning("⚠️ No reinforced weights available.")

# === 3. Pattern Combo Lookup ===
st.divider()
st.subheader("🔍 Check Pattern Eligibility")

signal_type = st.selectbox("Signal Type", ["Buy", "Sell", "Hold"])
strategy_name = st.selectbox("Strategy", ["Fusion", "LSTM", "Macro", "Sentiment"])

if label_df is not None:
    match = label_df[
        (label_df["Signal"] == signal_type) &
        (label_df["Strategy"] == strategy_name)
    ]
    if not match.empty:
        st.success(f"✅ Pattern '{signal_type} + {strategy_name}' is eligible for reinforcement.")
    else:
        st.info(f"ℹ️ Pattern '{signal_type} + {strategy_name}' has not been reinforced yet.")
        
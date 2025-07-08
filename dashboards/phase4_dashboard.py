import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Phase 4: Portfolio Intelligence", layout="wide")
st.title("🧠 Phase 4: Portfolio Learning & Risk Control")

def load_csv(path):
    return pd.read_csv(path) if os.path.exists(path) else None

# === 1. Final Signals (Vetoed) ===
st.subheader("🛑 Final Signals After Veto Logic")
veto_df = load_csv("logs/final_signals.csv")
if veto_df is not None and not veto_df.empty:
    st.dataframe(veto_df.sort_values("Confidence", ascending=False))
    st.caption(f"{len(veto_df)} signals approved as of {veto_df['Date'].max()}")
else:
    st.warning("⚠️ No final signals found.")

# === 2. Reinforced Strategy Weights ===
st.divider()
st.subheader("🧠 Reinforced Weights (Volatility-Aware)")
reinforce_df = load_csv("logs/strategy_weights_reinforced.csv")
if reinforce_df is not None:
    st.dataframe(reinforce_df.round(4))
    st.bar_chart(reinforce_df.set_index("Strategy")["Reinforced Weight"])
else:
    st.warning("⚠️ No reinforcement data found.")

# === 3. Rotation Engine Output ===
st.divider()
st.subheader("🔁 Portfolio Rotation Output")
rotated_df = load_csv("logs/rotated_weights.csv")
if rotated_df is not None:
    st.dataframe(rotated_df)
    st.bar_chart(rotated_df.set_index("Strategy")["Weight"])
else:
    st.info("ℹ️ No rotation applied (stable weights).")

# === 4. Capital-at-Risk Sizing ===
st.divider()
st.subheader("💼 Capital-at-Risk Position Sizing")
risk_df = load_csv("logs/capital_at_risk.csv")
if risk_df is not None:
    st.dataframe(risk_df.sort_values("Recommended Position Size", ascending=False))
    st.bar_chart(risk_df.set_index("Asset")["Recommended Position Size"])
else:
    st.warning("⚠️ No capital-at-risk output found.")

# Footer
st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")

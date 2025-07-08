import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Stress Test Report", layout="wide")
st.title("🧪 Adversarial Stress Testing Dashboard")

def load_csv(path):
    return pd.read_csv(path) if os.path.exists(path) else None

# === Adversarial Stress Test Results ===
st.subheader("📉 Strategy Resilience Under Simulated Stress")

stress_df = load_csv("logs/adversarial_test_report.csv")
if stress_df is not None and not stress_df.empty:
    st.dataframe(stress_df.round(3).sort_values("Success Rate", ascending=True))
    st.bar_chart(stress_df.set_index("Strategy")["Success Rate"])
    st.caption("Lower success rate under stress = higher fragility.")
else:
    st.warning("⚠️ No stress test results available. Run adversarial_tester first.")

# === Timestamp ===
st.caption(f"Last checked: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")

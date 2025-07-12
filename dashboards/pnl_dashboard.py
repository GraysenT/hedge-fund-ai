import streamlit as st
import pandas as pd
import os
import json
from utils.paths import TRADE_LOG_FILE

st.set_page_config(page_title="📈 Live PnL Tracker", layout="wide")
st.title("📈 Profit & Loss Dashboard")

# Load trade log
if not os.path.exists(TRADE_LOG_FILE):
    st.warning("Trade log not found.")
    st.stop()

with open(TRADE_LOG_FILE, "r") as f:
    try:
        logs = json.load(f)
    except Exception as e:
        st.error(f"Failed to parse trade log: {e}")
        st.stop()

# Parse into DataFrame
rows = []
for entry in logs:
    ts = entry.get("timestamp")
    for strat, result in entry.get("executions", {}).items():
        if isinstance(result, dict) and "side" in result:
            pnl = result.get("pnl", 0)
            rows.append({
                "timestamp": ts,
                "strategy": strat,
                "side": result.get("side"),
                "pnl": pnl
            })

if not rows:
    st.info("No PnL data available yet.")
    st.stop()

df = pd.DataFrame(rows)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# Cumulative PnL
df["cum_pnl"] = df["pnl"].cumsum()

# Layout
st.subheader("💰 Cumulative PnL Over Time")
st.line_chart(df.set_index("timestamp")["cum_pnl"])

st.subheader("🧾 Trade Log")
st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)
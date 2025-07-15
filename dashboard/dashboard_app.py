import streamlit as st
import pandas as pd
import os
import json
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Hedge Fund AI Dashboard", layout="wide")

st.title("📊 Hedge Fund AI Dashboard")

# === Live Sharpe Metrics ===
st.subheader("📈 Agent Performance (Latest)")

try:
    conn = sqlite3.connect("logs/sharpe_history.db")
    df = pd.read_sql_query("SELECT * FROM sharpe_scores", conn)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    latest = df.sort_values("timestamp").groupby("agent_name").last().reset_index()
    latest["Sharpe"] = latest["sharpe"]
    latest["Status"] = latest["sharpe"].apply(lambda s: "✅" if s > 0 else "⚠️")
    st.dataframe(latest[["agent_name", "Sharpe", "Status", "timestamp"]], use_container_width=True)
    conn.close()
except Exception as e:
    st.warning(f"Could not load Sharpe data: {e}")

# === Sharpe Ratio Chart ===
st.subheader("📉 Historical Sharpe Chart")

try:
    conn = sqlite3.connect("logs/sharpe_history.db")
    df = pd.read_sql_query("SELECT * FROM sharpe_scores", conn)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    chart_df = df.pivot(index="timestamp", columns="agent_name", values="sharpe")
    st.line_chart(chart_df)
    conn.close()
except Exception as e:
    st.warning(f"Chart unavailable: {e}")

# === Live Signal Logs ===
st.subheader("📡 Recent Signals")

signal_log_file = "logs/signals.jsonl"
if os.path.exists(signal_log_file):
    with open(signal_log_file, "r") as f:
        logs = [json.loads(line) for line in f if line.strip()]
    df = pd.DataFrame(logs).sort_values("timestamp", ascending=False)
    st.dataframe(df.head(50), use_container_width=True)
else:
    st.info("No signal logs found.")

# === Controls ===
st.subheader("🛠 Controls")
col1, col2 = st.columns(2)

with col1:
    if st.button("🧬 Trigger Evolution"):
        st.success("Evolution cycle started (stubbed)")

with col2:
    if st.button("🤖 Fork Top Agent"):
        st.success("Agent fork requested (stubbed)")

# === Refresh Toggle ===
refresh = st.checkbox("🔁 Auto-refresh every 30s", value=False)
if refresh:
    import time
    time.sleep(30)
    st.experimental_rerun()
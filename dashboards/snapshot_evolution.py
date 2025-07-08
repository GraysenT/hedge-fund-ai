import streamlit as st
import os
import json
import pandas as pd
import plotly.express as px

SNAPSHOT_DIR = "strategy_memory/history"

st.set_page_config(page_title="📈 Snapshot Evolution", layout="wide")
st.title("📈 Strategy Weight & PnL Evolution")

# Load all snapshots
data = []
for file in sorted(os.listdir(SNAPSHOT_DIR)):
    if not file.endswith(".json"):
        continue
    with open(os.path.join(SNAPSHOT_DIR, file), 'r') as f:
        snap = json.load(f)
        timestamp = snap["timestamp"]
        final = snap.get("final_weights", {})
        perf = snap.get("strategy_performance", {})
        for strategy, weight in final.items():
            entry = {
                "timestamp": timestamp,
                "strategy": strategy,
                "final_weight": weight
            }
            if isinstance(perf, dict):
                strat_perf = perf.get(strategy, {})
                entry["pnl"] = strat_perf.get("pnl")
                entry["sharpe"] = strat_perf.get("sharpe")
            data.append(entry)

if not data:
    st.warning("⚠️ No snapshot data available.")
    st.stop()

# Create DataFrame
history_df = pd.DataFrame(data)
history_df["timestamp"] = pd.to_datetime(history_df["timestamp"], format="%Y-%m-%d_%H-%M-%S")

# Sidebar filters
strategies = history_df["strategy"].unique().tolist()
selected = st.sidebar.multiselect("Select Strategies", strategies, default=strategies)
filtered_df = history_df[history_df["strategy"].isin(selected)]

# Plot weight evolution
fig_weight = px.line(
    filtered_df,
    x="timestamp",
    y="final_weight",
    color="strategy",
    markers=True,
    labels={"timestamp": "Date", "final_weight": "Final Weight"},
    title="Final Strategy Weights Over Time"
)
fig_weight.update_layout(legend_title_text="Strategy")

# Plot PnL evolution if present
if "pnl" in filtered_df.columns:
    fig_pnl = px.line(
        filtered_df.dropna(subset=["pnl"]),
        x="timestamp",
        y="pnl",
        color="strategy",
        markers=True,
        labels={"timestamp": "Date", "pnl": "PnL"},
        title="Strategy PnL Over Time"
    )
    fig_pnl.update_layout(legend_title_text="Strategy")
else:
    fig_pnl = None

# Render
st.plotly_chart(fig_weight, use_container_width=True)
if fig_pnl:
    st.plotly_chart(fig_pnl, use_container_width=True)

st.dataframe(filtered_df.sort_values(by="timestamp", ascending=False), use_container_width=True)

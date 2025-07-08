import streamlit as st
import json
import pandas as pd

st.title("🏁 Agent Leaderboard")

with open("agents/agent_tournament_results.json") as f:
    data = json.load(f)

df = pd.DataFrame([
    {
        "Agent": agent,
        "PnL": round(info["pnl"], 2),
        "Days": info["days"],
        "Strategies": len(info["strategies"]),
        "Status": "✅ Promoted" if info["pnl"] > 0 else "⚠️ Review"
    }
    for agent, info in data.items()
])

st.dataframe(df.sort_values(by="PnL", ascending=False))

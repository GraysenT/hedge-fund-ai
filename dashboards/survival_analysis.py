import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reinforcement.survival_tracker import load_snapshots, score_survival

st.set_page_config(page_title="🧠 Strategy Survival Analysis", layout="wide")
st.title("🧠 Generated Strategy Survival Analysis")

# Load and score
snapshots = load_snapshots()
df = score_survival(snapshots)

if df.empty:
    st.warning("No survival data found. Try generating and snapshotting new strategies.")
    st.stop()

# Filters
status_filter = st.sidebar.multiselect("Filter by Status", ["🔼 Promising", "➖ Neutral", "🔽 Decaying"], default=["🔼 Promising", "➖ Neutral", "🔽 Decaying"])
df_filtered = df[df["Status"].isin(status_filter)]

# Table
st.subheader("📋 Strategy Survival Table")
st.dataframe(df_filtered.sort_values(by="Avg Sharpe", ascending=False), use_container_width=True)

# Chart
st.subheader("📊 Avg Sharpe by Strategy")
fig = st.line_chart(df_filtered.set_index("Strategy")["Avg Sharpe"])

# Download
st.download_button(
    label="📥 Download Survival Scores",
    data=df_filtered.to_csv(index=False),
    file_name="strategy_survival_scores.csv",
    mime="text/csv"
)

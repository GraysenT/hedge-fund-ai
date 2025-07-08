import streamlit as st
import pandas as pd
import os

SNAPSHOT_FILE = "snapshots/allocation_history.csv"

st.set_page_config(page_title="📆 Allocation History", layout="wide")
st.title("📆 Strategy Allocation History")

if not os.path.exists(SNAPSHOT_FILE):
    st.warning("No snapshot data found.")
else:
    df = pd.read_csv(SNAPSHOT_FILE)
    df["date"] = pd.to_datetime(df["date"])

    st.markdown("### 📈 Daily Allocation Timeline by Strategy")
    pivot = df.pivot(index="date", columns="strategy", values="weight").fillna(0)
    st.line_chart(pivot)

    st.markdown("### 🧾 Allocation + Status Log")
    st.dataframe(df.sort_values(["date", "strategy"]).reset_index(drop=True).style.format({
        "weight": "{:.2%}"
    }))

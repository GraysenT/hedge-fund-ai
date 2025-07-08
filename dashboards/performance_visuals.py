import streamlit as st
import pandas as pd
from pathlib import Path

PERF = Path("performance_logs")

st.set_page_config(layout="wide")
st.title("📈 Strategy Performance Visuals")

files = list(PERF.glob("performance_*.csv"))
if files:
    df = pd.concat([pd.read_csv(f) for f in files])
    df["date"] = pd.to_datetime(df["date"])

    st.subheader("💹 Cumulative PnL by Strategy")
    cumulative = df.groupby(["date", "strategy"])["pnl"].sum().groupby(level=1).cumsum().reset_index()
    pivot = cumulative.pivot(index="date", columns="strategy", values="pnl").fillna(method="ffill")
    st.line_chart(pivot)

    st.subheader("⚖️ Capital Usage Heatmap")
    cap = df.pivot(index="date", columns="strategy", values="capital_used").fillna(0)
    st.dataframe(cap.style.background_gradient(cmap="PuBu"))
else:
    st.warning("No performance data available.")
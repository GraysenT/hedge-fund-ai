import streamlit as st
import pandas as pd
from pathlib import Path

SIGNAL_LOG_DIR = Path("signal_logs")  # Ensure signal logs are saved here
PERF_LOG_DIR = Path("performance_logs")  # From Phase 70

st.set_page_config(layout="wide")
st.title("📊 Signal vs. Actual Return Analysis")

def load_signals():
    files = list(SIGNAL_LOG_DIR.glob("signals_*.csv"))
    if not files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def load_performance():
    files = list(PERF_LOG_DIR.glob("performance_*.csv"))
    if not files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

signals_df = load_signals()
perf_df = load_performance()

if signals_df.empty or perf_df.empty:
    st.warning("Missing signal or performance logs.")
else:
    signals_df["date"] = pd.to_datetime(signals_df["date"])
    perf_df["date"] = pd.to_datetime(perf_df["date"])

    st.subheader("🧠 Signal Confidence vs. PnL Heatmap")

    merged = signals_df.merge(perf_df, on=["date", "strategy"])
    merged["confidence_bucket"] = pd.cut(merged["confidence"], bins=[0, 0.25, 0.5, 0.75, 1.0])

    heatmap = merged.groupby(["strategy", "confidence_bucket"])["pnl"].mean().unstack().fillna(0)
    st.dataframe(heatmap.style.background_gradient(cmap="coolwarm"))

    st.subheader("📉 Alpha Stability Over Time")
    pnl_trend = merged.groupby(["date", "strategy"])["pnl"].sum().reset_index()
    pivot = pnl_trend.pivot(index="date", columns="strategy", values="pnl").fillna(0)
    st.line_chart(pivot)

    st.subheader("📈 Predicted Signal vs. Realized Return Scatter")
    scatter_df = merged.copy()
    scatter_df = scatter_df.dropna(subset=["confidence", "pnl"])
    st.scatter_chart(scatter_df[["confidence", "pnl"]])
    
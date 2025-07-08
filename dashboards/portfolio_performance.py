import streamlit as st
import pandas as pd
from performance.performance_tracker import load_all_performance

st.set_page_config(layout="wide")
st.title("📈 Portfolio Performance Dashboard")

perf_df = load_all_performance()

if perf_df.empty:
    st.warning("No performance logs found.")
else:
    perf_df["date"] = pd.to_datetime(perf_df["date"])
    perf_df = perf_df.sort_values("date")

    st.subheader("💵 Total PnL Over Time")
    total_df = perf_df.groupby("date")["pnl"].sum().reset_index()
    st.line_chart(total_df.set_index("date"))

    st.subheader("📊 PnL by Strategy")
    strat_pnl = perf_df.pivot(index="date", columns="strategy", values="pnl").fillna(0)
    st.line_chart(strat_pnl)

    st.subheader("⚖️ Capital Usage by Strategy")
    strat_cap = perf_df.pivot(index="date", columns="strategy", values="capital_used").fillna(0)
    st.line_chart(strat_cap)

    if "sharpe" in perf_df.columns:
        st.subheader("📈 Sharpe Ratio by Strategy")
        sharpe_df = perf_df.dropna(subset=["sharpe"])
        strat_sharpe = sharpe_df.pivot(index="date", columns="strategy", values="sharpe")
        st.line_chart(strat_sharpe)
        
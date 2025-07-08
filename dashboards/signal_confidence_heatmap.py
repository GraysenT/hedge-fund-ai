import streamlit as st
import pandas as pd
from pathlib import Path

SIGNAL_LOG_DIR = Path("signal_logs")

st.set_page_config(layout="wide")
st.title("📊 Signal Confidence Heatmap & Filter")

def load_signals():
    files = list(SIGNAL_LOG_DIR.glob("signals_*.csv"))
    if not files:
        return pd.DataFrame()
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

signals_df = load_signals()

if signals_df.empty:
    st.warning("No signal logs found.")
else:
    if "date" in signals_df.columns:
        signals_df["date"] = pd.to_datetime(signals_df["date"])

    st.sidebar.header("🔎 Filter Options")
    strategy_options = signals_df["strategy"].dropna().unique().tolist()
    selected_strategies = st.sidebar.multiselect("Filter by Strategy", strategy_options, default=strategy_options)

    ticker_options = signals_df["ticker"].dropna().unique().tolist()
    selected_tickers = st.sidebar.multiselect("Filter by Ticker", ticker_options, default=ticker_options)

    signal_options = signals_df["signal"].dropna().unique().tolist()
    selected_signals = st.sidebar.multiselect("Filter by Signal Type", signal_options, default=signal_options)

    conf_range = st.sidebar.slider("Confidence Range", 0.0, 1.0, (0.0, 1.0), 0.01)

    filtered = signals_df[
        (signals_df["strategy"].isin(selected_strategies)) &
        (signals_df["ticker"].isin(selected_tickers)) &
        (signals_df["signal"].isin(selected_signals)) &
        (signals_df["confidence"].between(conf_range[0], conf_range[1]))
    ]

    st.subheader("🔥 Signal Confidence Distribution")
    if not filtered.empty:
        heatmap_df = (
            filtered.groupby(["strategy", "ticker"])["confidence"]
            .mean()
            .unstack()
            .fillna(0)
        )
        st.dataframe(heatmap_df.style.background_gradient(cmap="viridis"))
    else:
        st.info("No data matching filters.")

    st.subheader("📋 Filtered Signal Preview")
    st.dataframe(filtered.sort_values("date", ascending=False), use_container_width=True)
    
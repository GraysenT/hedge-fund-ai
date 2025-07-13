import streamlit as st
import pandas as pd
from core.strategy_performance import StrategyPerformance

st.set_page_config(layout="wide", page_title="Hedge Fund AI Dashboard")

def load_stats():
    # This should pull from a persistent performance store
    # For demo, we mock some data
    return {
        "TrendFollowing": {"pnl": 1000, "sharpe": 1.2},
        "MeanReversion": {"pnl": 800, "sharpe": 0.9},
        "Breakout": {"pnl": 500, "sharpe": 1.1}
    }

st.title("📈 Hedge Fund AI - Live Strategy Dashboard")
stats = load_stats()

df = pd.DataFrame(stats).T
st.dataframe(df.style.highlight_max(axis=0))
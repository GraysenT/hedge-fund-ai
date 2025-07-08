import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="📊 Performance Tracker", layout="wide")
st.title("📊 Strategy Performance Dashboard")

LOG_FILE = "trade_logs.csv"

if not os.path.exists(LOG_FILE):
    st.warning("No trade log file found yet.")
else:
    df = pd.read_csv(LOG_FILE, parse_dates=["timestamp"])
    df["date"] = df["timestamp"].dt.date

    st.markdown("### 💵 Cumulative Trades by Strategy")
    cumulative = df.groupby("strategy")["dollars"].sum().sort_values(ascending=False)
    st.bar_chart(cumulative)

    st.markdown("### 📆 Daily Trade Allocation")
    daily_alloc = df.groupby(["date", "strategy"])["dollars"].sum().unstack().fillna(0)
    st.line_chart(daily_alloc)

    st.markdown("### 🧠 Recent Trades (Last 20)")
    st.dataframe(df.sort_values("timestamp", ascending=False).head(20))

    st.markdown("### 🔍 Full Trade Log")
    st.dataframe(df.style.format({
        "price": "{:.2f}",
        "dollars": "${:.2f}",
        "qty": "{:,.0f}"
    }))

import streamlit as st
import json
import os
import pandas as pd
from utils.paths import STRATEGY_STATUS_FILE

st.set_page_config(page_title="📊 Strategy Performance", layout="wide")
st.title("📊 Strategy Performance Dashboard")

if not os.path.exists(STRATEGY_STATUS_FILE):
    st.warning("No performance data found.")
    st.stop()

with open(STRATEGY_STATUS_FILE, "r") as f:
    data = json.load(f)

if not data:
    st.info("No strategies scored yet.")
    st.stop()

df = pd.DataFrame.from_dict(data, orient="index").reset_index()
df = df.rename(columns={"index": "strategy"})
df = df.sort_values(by="sharpe", ascending=False)

st.dataframe(df, use_container_width=True)

st.subheader("📈 Sharpe Ratio Distribution")
st.bar_chart(df.set_index("strategy")["sharpe"])

st.subheader("✅ Top Performers")
st.write(df.head(5))

st.subheader("⚠️ Underperformers")
st.write(df.sort_values(by="sharpe").head(5))
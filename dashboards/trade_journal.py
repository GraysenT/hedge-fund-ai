import pandas as pd
import streamlit as st
from utils.paths import TRADE_LOG_FILE

st.set_page_config(page_title="📘 Trade Journal", layout="wide")

st.title("📘 Live Trade Journal")

try:
    df = pd.read_csv(TRADE_LOG_FILE)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values("Timestamp", ascending=False)
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Failed to load trade log: {e}")
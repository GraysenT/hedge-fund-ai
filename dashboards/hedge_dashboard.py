import streamlit as st
import pandas as pd
from pathlib import Path

LOG_PATH = Path("execution_logs/hedging_actions.csv")

st.set_page_config(layout="wide")
st.title("⚖️ Smart Hedging Dashboard")

if LOG_PATH.exists():
    df = pd.read_csv(LOG_PATH)
    st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

    st.subheader("📊 Exposure by Sector")
    st.bar_chart(df.groupby("sector")["exposure"].mean())
else:
    st.info("No hedging actions logged yet.")
    
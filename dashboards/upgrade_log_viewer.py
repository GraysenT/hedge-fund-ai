import streamlit as st
import pandas as pd
from pathlib import Path

LOG_PATH = Path("memory/upgrade_log.csv")

st.set_page_config(layout="wide")
st.title("🧠 Autonomous Upgrade Log")

if not LOG_PATH.exists():
    st.warning("No upgrade logs found.")
else:
    df = pd.read_csv(LOG_PATH)
    st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

    st.subheader("📊 Upgrades by Component")
    st.bar_chart(df["component"].value_counts())

    st.subheader("⏱️ Timeline of Upgrades")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    upgrades_over_time = df.groupby(df["timestamp"].dt.date).size()
    st.line_chart(upgrades_over_time)
    
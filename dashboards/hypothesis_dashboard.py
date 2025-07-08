import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("🧪 Hypothesis Test Results")

HYP_PATH = Path("memory/hypothesis_results.csv")

if HYP_PATH.exists():
    df = pd.read_csv(HYP_PATH)
    st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

    st.subheader("📈 Pass Rate by Idea Type")
    df["type"] = df["idea"].apply(lambda x: x.split()[0])
    st.bar_chart(df.groupby("type")["result"].apply(lambda x: (x == "pass").mean()))
else:
    st.info("No hypothesis results yet.")
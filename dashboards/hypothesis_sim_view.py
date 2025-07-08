import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("🧪 Live Hypothesis Simulation Viewer")

log_path = Path("simulation/hypothesis_sim_log.csv")
if log_path.exists():
    df = pd.read_csv(log_path)
    st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

    st.subheader("Strategy Count")
    st.bar_chart(df["strategy"].value_counts())
else:
    st.info("No simulated hypothesis signals yet.")
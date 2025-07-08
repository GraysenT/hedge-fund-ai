import streamlit as st
import pandas as pd
from backtest.backtester import run_backtest

st.set_page_config(layout="wide")
st.title("🧪 Backtest & Performance Summary")

st.subheader("Run Live Backtest")
if st.button("▶️ Run Backtest"):
    results = run_backtest()
    if results is not None:
        st.dataframe(results, use_container_width=True)

st.markdown("---")
st.subheader("📂 Backtest Reports")

from pathlib import Path
report_files = list(Path("reports").glob("backtest_summary_*.csv"))

if report_files:
    selected = st.selectbox("View Report:", [f.name for f in report_files])
    df = pd.read_csv(Path("reports") / selected)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No reports found.")
    
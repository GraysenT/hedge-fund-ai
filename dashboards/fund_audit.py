import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("📘 Fund Audit Trail")

log_path = Path("audit/fund_balance.csv")

if log_path.exists():
    df = pd.read_csv(log_path)
    df["date"] = pd.to_datetime(df["date"])
    st.line_chart(df.set_index("date")["balance"])
    st.subheader("🔍 Latest Balance")
    st.metric("Fund Value", f"${df['balance'].iloc[-1]:,.2f}")
else:
    st.info("No fund tracking data yet.")
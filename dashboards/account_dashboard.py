import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("💼 Multi-Account Strategy Dashboard")

accounts = ["main_fund", "hedge_fund_alpha", "crypto_overlay"]
selected = st.selectbox("Select Account", accounts)

log_folder = Path(f"execution_logs/{selected}")
files = list(log_folder.glob("trades_*.csv"))

if files:
    df = pd.concat([pd.read_csv(f) for f in files])
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df["strategy"].value_counts())
else:
    st.warning(f"No trades logged for {selected} yet.")
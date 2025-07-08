import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("📊 PnL Attribution Report")

path = Path("reports/pnl_attribution.csv")

if path.exists():
    df = pd.read_csv(path)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("strategy")["pnl"])
else:
    st.warning("Attribution report not found.")
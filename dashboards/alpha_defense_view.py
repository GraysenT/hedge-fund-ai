import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("🛡️ Alpha Defense Status")

path = Path("memory/alpha_defense_status.csv")
if path.exists():
    df = pd.read_csv(path)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("strategy")["avg_pnl"])
else:
    st.warning("No alpha defense status available.")
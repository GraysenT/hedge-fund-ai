import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("⚖️ Portfolio Optimizer: Strategy Allocation")

path = Path("memory/optimized_weights.csv")

if path.exists():
    df = pd.read_csv(path)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("strategy")["weight"])
else:
    st.warning("No optimized weight file found yet.")
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout="wide")
st.title("🧠 Meta-Strategy Blender View")

path = Path("memory/meta_blended_weights.csv")

if path.exists():
    df = pd.read_csv(path)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("strategy")["weight"])
else:
    st.warning("Meta strategy blend file not found yet.")
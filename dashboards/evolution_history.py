import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Strategy Evolution Timeline", layout="wide")

st.title("🧬 Strategy Evolution History")

try:
    with open("mutation_log.json") as f:
        mutations = json.load(f)
except FileNotFoundError:
    mutations = []

if not mutations:
    st.warning("No mutation history found.")
else:
    df = pd.DataFrame(mutations)
    df = df.sort_values("timestamp", ascending=False)
    st.dataframe(df.style.highlight_max(axis=0))
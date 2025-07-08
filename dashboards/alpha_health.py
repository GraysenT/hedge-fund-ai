import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alpha Health", layout="wide")

st.title("🧠 Alpha Health Monitor")

# Placeholder data
alpha_scores = pd.DataFrame({
    "Strategy": ["LSTM", "TrendAlpha", "MacroEdge", "StatArb"],
    "Score": [0.87, 0.74, 0.68, 0.91],
    "Promoted": [True, False, False, True],
    "Muted": [False, False, True, False]
})

st.dataframe(alpha_scores.style
    .background_gradient(subset=["Score"], cmap='Greens')
    .applymap(lambda x: 'color: red' if x is True else '')
)
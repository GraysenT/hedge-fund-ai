import streamlit as st, pandas as pd, os, json

def render_dream_tab():
    all_dreams = []
    for file in os.listdir("logs/dream_logs"):
        with open(f"logs/dream_logs/{file}") as f:
            data = json.load(f)
            all_dreams.extend([(d["sharpe"], file) for d in data])
    df = pd.DataFrame(all_dreams, columns=["Sharpe", "Dream"])
    st.line_chart(df["Sharpe"])
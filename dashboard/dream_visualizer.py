import streamlit as st
import pandas as pd
import json

st.set_page_config(layout="wide", page_title="Dream Visualizer")
st.title("💭 Historical Dream Explorer")

dreams = []
with open("logs/dreams.jsonl") as f:
    for line in f:
        dreams.append(json.loads(line))

df = pd.DataFrame(dreams)
df["timestamp"] = pd.to_datetime(df["context"].apply(lambda c: c.get("timestamp", "")), errors="coerce")
df["delta"] = df["future_price"] - df["context"].apply(lambda c: c.get("price", 0))

st.line_chart(df["future_price"], height=300, use_container_width=True)
st.bar_chart(df["delta"], height=200, use_container_width=True)

st.subheader("🔍 Raw Dreams")
st.dataframe(df[["context", "future_price", "imagined_outcome"]].tail(10))
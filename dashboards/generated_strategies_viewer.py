import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px

GEN_PATH = "strategy_memory/generated_strategies.json"

st.set_page_config(page_title="🧬 Generated Strategies", layout="wide")
st.title("🧬 Generated Strategy Viewer")

if not os.path.exists(GEN_PATH):
    st.warning("No generated strategies found. Please run strategy_generator.py.")
    st.stop()

with open(GEN_PATH, 'r') as f:
    gen_strategies = json.load(f)

strategies = list(gen_strategies.keys())
selected = st.selectbox("Select Generated Strategy", strategies)

weights = gen_strategies[selected]
df = pd.DataFrame(weights.items(), columns=["Original Strategy", "Weight"]).sort_values(by="Weight", ascending=False)

st.subheader(f"📊 Allocation Breakdown – {selected}")
st.dataframe(df, use_container_width=True)

fig = px.bar(df, x="Original Strategy", y="Weight", title=f"{selected} Weights")
st.plotly_chart(fig, use_container_width=True)

st.download_button(
    label="📥 Download This Strategy",
    data=json.dumps({selected: weights}, indent=2),
    file_name=f"{selected}.json",
    mime="application/json"
)

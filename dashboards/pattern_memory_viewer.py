import streamlit as st
from reinforcement.pattern_memory import load_pattern_memory

st.set_page_config(layout="wide")
st.title("🧠 Strategy Pattern Memory")

df = load_pattern_memory()

if df.empty:
    st.warning("No pattern memory data found.")
else:
    st.dataframe(df.sort_values("fragility_rate"), use_container_width=True)

    st.subheader("📉 Fragility Rate by Strategy")
    st.bar_chart(df.set_index("strategy")["fragility_rate"])

    st.subheader("📈 Anti-Fragile Bounces (Recovery After Failure)")
    st.bar_chart(df.set_index("strategy")["anti_fragile_bounces"])
    
import streamlit as st
from gpt_copilot import gpt_copilot_converse

st.title("🧠 GPT Co-Pilot (Dual Consciousness Terminal)")
query = st.text_input("Ask a question or command...")

if st.button("Submit"):
    if query.strip():
        gpt_copilot_converse(query)
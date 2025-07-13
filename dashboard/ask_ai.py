import streamlit as st
from intelligence.query_layer import ask_intelligence

st.title("🧠 Ask the AI")

question = st.text_area("What do you want to know?")
if st.button("Ask"):
    response = ask_intelligence(question)
    st.write("🤖 Response:")
    st.write(response)
import streamlit as st
from worldbuilder.economy_sim import EconomySim

st.set_page_config(layout="wide", page_title="Recursive AI Economy")
st.title("🏛 Recursive AI Economy")

if "sim" not in st.session_state:
    st.session_state.sim = EconomySim(seeds=20)

if st.button("🔁 Tick Simulation"):
    st.session_state.sim.step()

top = st.session_state.sim.top()
st.subheader("🏆 Top Ventures")
for seed in top:
    st.markdown(f"**{seed.vision}** — Capital: ${round(seed.capital, 2)}")
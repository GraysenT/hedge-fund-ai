import streamlit as st

st.set_page_config(page_title="Global Control", layout="wide", initial_sidebar_state="expanded")

st.title("🚀 Global Control Center")

mode = st.radio("Trading Mode:", ["Simulation", "Paper", "Live"], index=1)
st.write(f"### Mode Selected: {mode}")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🧠 Active Strategies", 18)
    st.metric("🔥 Live Signals", 6)
with col2:
    st.metric("📈 System PnL", "$15,480", delta="+2.4%")
    st.metric("⚙️ Execution Latency", "47 ms")
with col3:
    st.metric("🧪 Backtests Running", 3)
    st.metric("📊 Alpha Memory Usage", "89%")

st.button("🔄 Restart Strategy Engine")
st.button("🛑 Emergency Kill Switch")

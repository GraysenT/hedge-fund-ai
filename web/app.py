import streamlit as st
import requests

st.set_page_config(page_title="Fund Dashboard", layout="wide")

st.title("📈 Fund Intelligence Dashboard")

cap = requests.get("http://localhost:8000/capital").json()
orders = requests.get("http://localhost:8000/orders").json()
agents = requests.get("http://localhost:8000/agents").json()

st.header("💸 Capital Allocation")
st.json(cap)

st.header("📜 Recent Orders")
st.json(orders)

st.header("🤖 Agents")
for agent, strats in agents.items():
    st.write(f"🧠 {agent}: {len(strats)} strategies")
    
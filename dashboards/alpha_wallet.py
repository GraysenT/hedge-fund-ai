import streamlit as st
import json
import os

st.set_page_config(page_title="Alpha Wallet", layout="centered")
st.title("💼 Client Alpha Wallet")

client_id = st.selectbox("Select Client", ["client_alpha", "client_beta"])
allocs = json.load(open("memory/client_allocations/" + sorted(os.listdir("memory/client_allocations"))[-1]))
perf = json.load(open("memory/performance/" + sorted(os.listdir("memory/performance"))[-1]))

if client_id not in allocs:
    st.warning("No allocations yet.")
else:
    strategies = allocs[client_id].keys()
    st.subheader("📊 Strategy Performance")
    for strat in strategies:
        if strat in perf:
            p = perf[strat]
            st.write(f"**{strat}**: ${round(p['pnl'],2)} | {round(p['return_pct']*100,2)}%")

    total_pnl = sum(perf[s]["pnl"] for s in strategies if s in perf)
    fee = round(total_pnl * 0.1, 2)
    st.subheader(f"💰 Net PnL: ${round(total_pnl,2)} | Fee Due: ${fee}")

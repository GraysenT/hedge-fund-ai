import streamlit as st
import json
import os

st.set_page_config(page_title="Fund Mobile", layout="centered")

st.title("📈 Fund Snapshot")

latest_perf = sorted(os.listdir("memory/performance"))[-1]
pnl = json.load(open(f"memory/performance/{latest_perf}"))

st.header("💹 PnL")
for strat, res in pnl.items():
    st.write(f"{strat}: ${round(res['pnl'],2)} | {round(res['return_pct']*100, 2)}%")

latest_alloc = sorted(os.listdir("memory/scaled_allocations"))[-1]
alloc = json.load(open(f"memory/scaled_allocations/{latest_alloc}"))

st.header("💸 Capital Allocation")
for strat, val in alloc.items():
    st.write(f"{strat}: ${round(val * 1_000_000, 2)}")
    
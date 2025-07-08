import streamlit as st
import os
import json

st.set_page_config(page_title="📊 Hedge Fund AI Overview", layout="wide")
st.title("📊 Hedge Fund AI System Overview")

# Load recent capital allocation
alloc_file = sorted(os.listdir("memory/scaled_allocations"))[-1]
alloc = json.load(open(f"memory/scaled_allocations/{alloc_file}"))

# Load recent performance
perf_file = sorted(os.listdir("memory/performance"))[-1]
perf = json.load(open(f"memory/performance/{perf_file}"))

st.header("💸 Capital Allocation")
st.json(alloc)

st.header("📈 Strategy Performance")
st.json(perf)

# Firewalled strategies
if os.path.exists("meta/alpha_firewall.json"):
    firewalled = json.load(open("meta/alpha_firewall.json"))
    st.warning(f"🚫 Firewalled Strategies: {', '.join(firewalled)}")

# Self-confidence logs
if os.path.exists("meta/self_confidence_log.json"):
    st.header("🧠 Self-Confidence Ratings")
    logs = open("meta/self_confidence_log.json").read().splitlines()
    for line in logs[-3:]:
        st.text(line)

# Proposals
proposal_dir = "meta/proposals"
if os.path.exists(proposal_dir):
    st.header("📜 AI Governance Proposals")
    for f in sorted(os.listdir(proposal_dir))[-3:]:
        with open(os.path.join(proposal_dir, f)) as proposal_file:
            st.markdown(proposal_file.read())
            
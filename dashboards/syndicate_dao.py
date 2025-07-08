import streamlit as st
import json
import os

st.set_page_config(page_title="Syndicate DAO", layout="wide")
st.title("🗳 Syndicate Governance Dashboard")

PROPOSALS_PATH = "agents/syndicates/proposals/"

if not os.path.exists(PROPOSALS_PATH):
    st.warning("No proposals yet.")
else:
    proposals = sorted(os.listdir(PROPOSALS_PATH))[-5:]

    for prop_file in proposals:
        prop = json.load(open(f"{PROPOSALS_PATH}/{prop_file}"))
        st.subheader(f"📜 Proposal: {prop['strategy']}")
        st.text(prop["summary"])
        with st.form(f"form_{prop_file}"):
            votes = {}
            for agent in prop["votes"]:
                votes[agent] = st.selectbox(f"{agent} vote", ["yes", "no"], index=0)
            submit = st.form_submit_button("Submit Vote")
            if submit:
                prop["votes"] = votes
                json.dump(prop, open(f"{PROPOSALS_PATH}/{prop_file}", "w"), indent=2)
                st.success("✅ Vote submitted.")
                
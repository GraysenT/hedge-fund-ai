import streamlit as st
import json
from utils.paths import OVERRIDE_FILE

st.set_page_config(layout="wide", page_title="🔧 Manual Override Control")

st.title("🔧 Strategy Override Control Panel")

st.info("Use this to manually boost, mute, or reroute strategies.")

with st.form("override_form"):
    strategy = st.text_input("Strategy name")
    boost = st.slider("Boost Weight (0 = muted, 1 = normal, 2 = x2)", 0.0, 2.0, 1.0)
    note = st.text_area("Reason / Comment")
    submit = st.form_submit_button("Save Override")

    if submit and strategy:
        overrides = {}
        try:
            with open(OVERRIDE_FILE, "r") as f:
                overrides = json.load(f)
        except:
            pass

        overrides[strategy] = {"boost": boost, "note": note}
        with open(OVERRIDE_FILE, "w") as f:
            json.dump(overrides, f, indent=2)
        st.success(f"Override saved for {strategy}")
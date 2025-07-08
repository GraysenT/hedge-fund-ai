import streamlit as st
import os
import importlib.util

st.set_page_config(page_title="Plugin Vault", layout="wide")
st.title("🔒 Internal Strategy Vault")

plugins = [f for f in os.listdir("plugins") if f.endswith(".py")]
selected = st.selectbox("Choose a strategy", plugins)

if st.button("🧪 Backtest"):
    path = f"plugins/{selected}"
    spec = importlib.util.spec_from_file_location("vault_plugin", path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        if hasattr(mod, "run"):
            result = mod.run()
            st.success(f"✅ Backtest Result: {result}")
        else:
            st.warning("⚠️ No run() method found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
        
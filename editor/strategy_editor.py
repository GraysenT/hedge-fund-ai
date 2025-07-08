import streamlit as st
import os
import traceback
from nlp.strategy_compiler import run_in_sandbox, save_strategy

st.set_page_config(page_title="📘 Strategy Editor", layout="wide")

st.title("🧠 Strategy Code Editor")

strategy_name = st.text_input("Strategy name (no spaces):", "custom_strategy")
default_code = '''def run():
    print("BUY AAPL if close > MA(10)")'''

code = st.text_area("Strategy Code", default_code, height=300)

if st.button("✅ Validate & Run"):
    try:
        save_strategy(code, strategy_name)
        run_in_sandbox(strategy_name)
        st.success(f"✅ Saved and executed `{strategy_name}` successfully.")
    except Exception as e:
        st.error(f"❌ Error: {traceback.format_exc()}")

import streamlit as st

def enable_dark_mode():
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #0E1117;
            color: #D1D5DB;
        }
        .stDataFrame thead {
            background-color: #1F2937;
        }
        .css-1aumxhk {
            color: #E5E7EB;
        }
        </style>
    """, unsafe_allow_html=True)
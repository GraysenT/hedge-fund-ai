import streamlit as st
from reporting.report_generator import generate_full_report

st.set_page_config(layout="wide")
st.title("📄 Generate Investor Report")

if st.button("📈 Generate PDF Report"):
    generate_full_report()
    st.success("Report generated and saved to /reports/generated/")
    
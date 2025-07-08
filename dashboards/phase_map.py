import streamlit as st
from pathlib import Path

st.set_page_config(page_title="📘 Phase Map & Program Timeline", layout="wide")

st.title("📘 System Phase Map & Roadmap")

st.markdown("### 🧠 Current Status Summary")
st.info("""
All core intelligence layers (Phases 1–7) are **fully completed** and operational.

The system is now scaling Phase 8 for speed, power, and low-latency optimization — while Phases 9–13 are queued for global intelligence, portfolio AI, monetization, and long-term autonomy.
""")

# ✅ Correct local path to your Markdown document
doc_path = Path("docs/full_phase_outline.md")

# 🔍 Debug helper: show the resolved path
st.write("📂 Looking for:", doc_path.resolve())

st.markdown("### 🔗 Full Outline Document")
if doc_path.exists():
    st.download_button(
        "📄 Download Full Phase Outline",
        data=doc_path.read_text(),
        file_name="full_phase_outline.md"
    )
else:
    st.error("❌ Document not found at: " + str(doc_path.resolve()))

st.markdown("### 🧭 Phase Timeline")

phases = [
    ("Phase 1", "✅ Core Prediction & Signal Engine", "Completed"),
    ("Phase 2", "✅ Execution, Alerts & Trading Automation", "Completed"),
    ("Phase 3", "✅ Strategy Intelligence & Adaptive Allocation", "Completed"),
    ("Phase 4", "✅ Portfolio Learning & Risk Control", "Completed"),
    ("Phase 5", "✅ Advanced Evolution & Intelligence", "Completed"),
    ("Phase 6", "✅ Autonomous Research & Self-Expansion", "Completed"),
    ("Phase 7", "✅ Governance, Risk & Deployment Oversight", "Completed"),
    ("Phase 8", "🔄 Performance Amplification & Latency Optimization", "In Progress"),
    ("Phase 9", "🔄 Global Intelligence & Cross-Market Awareness", "Queued"),
    ("Phase 10", "🔄 Portfolio AI & Fund-Level Logic", "Queued"),
    ("Phase 11", "🔄 Monetization & Strategic Output", "Queued"),
    ("Phase 12", "🔄 Full Autonomy, Defense & Auditing", "Queued"),
    ("Phase 13+", "🧠 Experimental Frontier / AI X-Lab", "Optional"),
]

st.markdown("#### 📆 Phase Progress Overview")
for label, title, status in phases:
    emoji = "✅" if "Completed" in status else "🔄" if "In Progress" in status else "🕒"
    st.markdown(f"**{emoji} {label}:** {title} — *{status}*")

st.markdown("### 📍 Next Up")
st.success("→ Phase 8 continues scaling. Phase 9 (global macro intelligence) will follow.")

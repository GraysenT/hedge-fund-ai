import seaborn as sns
import streamlit as st
import importlib
import sys
import os
import datetime
import pandas as pd
import random
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(page_title="Live Signal Viewer", layout="wide")
st.title("📈 Hedge Fund AI – Live Signal Viewer + PnL Tracker")

# === FUSED SIGNALS (From Phase 2) ===
try:
    fusion_module = importlib.import_module(
        "signal_fusion.signal_fusion_engine")
    st.success("✅ Signal Fusion Engine Loaded")

    st.subheader("🧠 Fused Signals – Real-Time Output")

    # Simulated blend logic
    lstm = {"Gold": 0.78, "Oil": 0.61, "Wheat": 0.73, "Cattle": 0.69}
    sentiment = {"Gold": 0.7, "Oil": 0.4, "Wheat": 0.8, "Cattle": 0.6}
    macro = {"Gold": 1.0, "Oil": 0.5, "Wheat": 0.6, "Cattle": 0.4}

    st.write("### Final Signal Decisions")
    for asset in lstm:
        score = round(0.5 * lstm[asset] + 0.3 *
                      sentiment[asset] + 0.2 * macro[asset], 2)
        signal = "Buy" if score >= 0.7 else "Hold" if score >= 0.5 else "Sell"
        st.metric(label=f"{asset}", value=signal, delta=f"Confidence: {score}")

except Exception as e:
    st.error(f"❌ Error loading fusion engine: {e}")

# === PNL CHART (Simulated) ===
st.divider()
st.subheader("📊 Simulated Strategy PnL (Demo)")

# Simulate some dummy PnL data for display
dates = pd.date_range(end=datetime.datetime.now(), periods=14).tolist()
pnl_values = [round(random.uniform(-200, 600), 2) for _ in dates]
pnl_df = pd.DataFrame({'Date': dates, 'PnL': pnl_values})

# Plotting with Streamlit + Matplotlib
fig, ax = plt.subplots()
ax.plot(pnl_df['Date'], pnl_df['PnL'], marker='o', linestyle='-')
ax.axhline(y=0, color='gray', linestyle='--')
ax.set_title("Simulated Daily Net PnL")
ax.set_xlabel("Date")
ax.set_ylabel("PnL ($)")
plt.xticks(rotation=45)

st.pyplot(fig)


st.divider()
st.subheader("🌡 Signal Confidence Heatmap")

# Simulate confidence matrix for heatmap
confidence_matrix = {
    "Gold": [round(random.uniform(0.6, 0.95), 2)],
    "Oil": [round(random.uniform(0.5, 0.9), 2)],
    "Wheat": [round(random.uniform(0.55, 0.97), 2)],
    "Cattle": [round(random.uniform(0.4, 0.85), 2)]
}

df_heatmap = pd.DataFrame(confidence_matrix, index=["Confidence"])

fig2, ax2 = plt.subplots()
sns.heatmap(df_heatmap, annot=True, cmap="YlGnBu",
            vmin=0.0, vmax=1.0, linewidths=0.5, ax=ax2)
ax2.set_title("Model Confidence Across Commodities")
st.pyplot(fig2)

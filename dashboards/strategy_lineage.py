import os
import json
import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import pandas as pd

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
EXPORT_JSON = "strategy_memory/exported_lineage.json"
EXPORT_GEXF = "strategy_memory/exported_lineage.gexf"

st.set_page_config(page_title="🧬 Strategy Lineage Tree", layout="wide")
st.title("🧬 Strategy Genetic Lineage Viewer")

if not os.path.exists(LINEAGE_PATH):
    st.warning("No strategy_lineage.json found. Please run lineage_tracker.py first.")
    st.stop()

with open(LINEAGE_PATH, 'r') as f:
    lineage = json.load(f)

if not lineage:
    st.warning("Lineage file is empty.")
    st.stop()

# Optional: Filter by generation depth
max_depth = max(meta.get("depth", 0) for meta in lineage.values())
depth_range = st.sidebar.slider("Filter by Depth", 0, max_depth, (0, max_depth))

# Optional: toggle coloring mode
color_mode = st.sidebar.radio("Color nodes by", ["Rating", "Sharpe"])

# Export buttons
st.sidebar.markdown("---")
if st.sidebar.button("📥 Export Lineage as JSON"):
    with open(EXPORT_JSON, 'w') as f:
        json.dump(lineage, f, indent=2)
    st.sidebar.success("Lineage exported as JSON")

if st.sidebar.button("📥 Export Lineage as GEXF"):
    G_export = nx.DiGraph()
    for child, meta in lineage.items():
        parent = meta.get("parent")
        if parent:
            G_export.add_edge(parent, child)
        G_export.add_node(child, **meta)
    nx.write_gexf(G_export, EXPORT_GEXF)
    st.sidebar.success("Lineage exported as GEXF (for Gephi or Cytoscape)")

# Build graph
G = nx.DiGraph()
for child, meta in lineage.items():
    if not (depth_range[0] <= meta.get("depth", 0) <= depth_range[1]):
        continue
    parent = meta.get("parent")
    if parent:
        G.add_edge(parent, child)
    G.add_node(child, **meta)

# Generate positions using layout
pos = nx.spring_layout(G, k=0.5, iterations=100)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=1, color='#888'),
    hoverinfo='none',
    mode='lines'
)

node_x = []
node_y = []
node_text = []
node_color = []
sharpe_scores_by_depth = {}
node_counts_by_depth = {}
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    meta = G.nodes[node]
    depth = meta.get("depth", '?')
    rating = meta.get("rating", '🟡 Unknown')
    sharpe = meta.get("sharpe", 0)
    label = f"{node}\nDepth: {depth}\n{rating}\nSharpe: {sharpe}"
    node_text.append(label)

    if color_mode == "Rating":
        color = '#1f77b4'
        if rating == "🟢 Strong":
            color = "green"
        elif rating == "🔴 Retire":
            color = "red"
        elif rating == "🟡 Watch":
            color = "orange"
    else:  # color by Sharpe
        if sharpe >= 1.0:
            color = "green"
        elif sharpe < 0.3:
            color = "red"
        else:
            color = "orange"

    node_color.append(color)

    if isinstance(depth, int):
        sharpe_scores_by_depth.setdefault(depth, 0)
        node_counts_by_depth.setdefault(depth, 0)
        sharpe_scores_by_depth[depth] += sharpe
        node_counts_by_depth[depth] += 1

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers+text',
    text=node_text,
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        showscale=False,
        color=node_color,
        size=14,
        line_width=2
    )
)

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Strategy Lineage Graph',
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=False, zeroline=False)
                ))

st.plotly_chart(fig, use_container_width=True)

# Optional table for inspection
df = pd.DataFrame.from_dict(lineage, orient='index')
df.index.name = "Strategy"
df = df.reset_index().sort_values(by="depth")
st.subheader("📋 Lineage Metadata Table")
st.dataframe(df, use_container_width=True)

# Mutation performance trend
if sharpe_scores_by_depth:
    st.subheader("📈 Avg Sharpe by Mutation Depth")
    sharpe_trend = pd.DataFrame({
        "Depth": list(sharpe_scores_by_depth.keys()),
        "Avg Sharpe": [sharpe_scores_by_depth[d] / node_counts_by_depth[d] for d in sharpe_scores_by_depth]
    }).sort_values(by="Depth")
    st.line_chart(sharpe_trend.set_index("Depth"))
    
# app.py
# ─────────────────────────────────────────────────────────────────────────────
# DIU Campus Navigation System — Streamlit Entry Point
# ─────────────────────────────────────────────────────────────────────────────
import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from graph.graph_data         import NODES, EDGES, GRAPH
from graph.dijkstra           import dijkstra
from graph.path_utils         import reconstruct_path, format_path, path_total_distance
from visualization.graph_plot import draw_campus_graph
from visualization.animation  import animate_path


# ═════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="DIU Campus Navigation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── App background ── */
.stApp { background-color: #0F0F1A; }

/* ── General text ── */
h1, h2, h3, h4, p, label,
.stMarkdown, .stText       { color: #E0E0FF !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"]  { background-color: #14142A !important; }

/* ── Divider ── */
hr { border-color: #2A2A4A; }

/* ── Path display box ── */
.path-box {
    background   : #1A1A2E;
    border       : 1px solid #4FC3F7;
    border-left  : 4px solid #FFD700;
    border-radius: 10px;
    padding      : 14px 18px;
    font-size    : 15px;
    color        : #FFD700;
    font-weight  : bold;
    line-height  : 2;
    word-break   : break-word;
}

/* ── Metric card ── */
.metric-card {
    background   : #1A1A2E;
    border       : 1px solid #2A2A4A;
    border-radius: 12px;
    padding      : 16px 10px;
    text-align   : center;
}
.metric-value  { font-size: 28px; font-weight: bold; color: #00E676; }
.metric-label  { font-size: 11px; color: #90CAF9; margin-top: 4px; }

/* ── Info banner ── */
.info-banner {
    background   : #0D2137;
    border       : 1px solid #0D47A1;
    border-radius: 8px;
    padding      : 10px 16px;
    color        : #90CAF9;
    font-size    : 13px;
}
</style>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# HEADER
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("# 🎓 DIU Campus Navigation System")
st.markdown(
    "<p style='color:#90CAF9; font-size:15px; margin-top:-10px;'>"
    "Find the shortest route between any two campus locations using "
    "<b>Dijkstra's Algorithm</b>.</p>",
    unsafe_allow_html=True,
)
st.divider()


# ═════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## 🗺️ Route Planner")
    st.markdown(
        "<p style='font-size:13px; color:#90CAF9;'>"
        "Choose your start and destination, then press <b>Find Shortest Path</b>."
        "</p>",
        unsafe_allow_html=True,
    )

    start_node = st.selectbox("📍 Start Location",  NODES, index=0)
    end_node   = st.selectbox("🏁 Destination",     NODES, index=10)

    st.divider()

    anim_speed = st.slider(
        "⏱️ Animation Speed (sec / step)",
        min_value=0.2,
        max_value=2.5,
        value=0.8,
        step=0.1,
        help="Lower = faster animation",
    )

    find_btn = st.button(
        "🔍  Find Shortest Path",
        use_container_width=True,
        type="primary",
    )

    st.divider()

    # About box
    st.markdown("""
    <div class="info-banner">
    <b>📘 About Dijkstra's Algorithm</b><br><br>
    Dijkstra's algorithm computes the <i>shortest path</i> from one node to
    all others in a weighted graph.<br><br>
    It uses a <b>min-heap (priority queue)</b> to always process the
    nearest unvisited node, guaranteeing the globally optimal result for
    non-negative edge weights.<br><br>
    <b>Complexity:</b> O((V + E) log V)
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# ROUTE COMPUTATION  (triggered by button)
# ═════════════════════════════════════════════════════════════════════════════
if find_btn:
    if start_node == end_node:
        st.warning("⚠️ Start and destination are the same. Please choose different locations.")
    else:
        with st.spinner("⚙️ Running Dijkstra's algorithm…"):
            distances, previous = dijkstra(GRAPH, start_node)
            path = reconstruct_path(previous, start_node, end_node)

        if not path:
            st.error(
                f"❌ No path found between **{start_node}** and **{end_node}**. "
                "They may not be connected in the current graph."
            )
        else:
            total_dist = distances[end_node]

            # Persist results across tab switches
            st.session_state["path"]       = path
            st.session_state["start"]      = start_node
            st.session_state["end"]        = end_node
            st.session_state["dist"]       = total_dist
            st.session_state["distances"]  = distances
            st.session_state["anim_speed"] = anim_speed


# ═════════════════════════════════════════════════════════════════════════════
# TABS
# ═════════════════════════════════════════════════════════════════════════════
tab_graph, tab_anim, tab_table = st.tabs([
    "📊  Graph & Path",
    "🎬  Step Animation",
    "📋  All Distances",
])


# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — Graph View + Path Result
# ─────────────────────────────────────────────────────────────────────────────
with tab_graph:
    has_result = "path" in st.session_state

    if has_result:
        path       = st.session_state["path"]
        start      = st.session_state["start"]
        end        = st.session_state["end"]
        total_dist = st.session_state["dist"]

        # ── Metrics row ───────────────────────────────────────────────────────
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f"<div class='metric-card'>"
                f"<div class='metric-value'>{len(path) - 1}</div>"
                f"<div class='metric-label'>🔗 HOPS</div></div>",
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"<div class='metric-card'>"
                f"<div class='metric-value'>{total_dist}</div>"
                f"<div class='metric-label'>📏 TOTAL DISTANCE (units)</div></div>",
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f"<div class='metric-card'>"
                f"<div class='metric-value'>{len(path)}</div>"
                f"<div class='metric-label'>📍 LOCATIONS VISITED</div></div>",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Path text ─────────────────────────────────────────────────────────
        st.markdown("### 🗺️ Shortest Path")
        st.markdown(
            f"<div class='path-box'>{format_path(path)}</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)

        # ── Static highlighted graph ──────────────────────────────────────────
        st.markdown("### 🖼️ Campus Map — Path Highlighted")
        fig = draw_campus_graph(
            edges=EDGES,
            path=path,
            highlight_nodes=set(path),
            title=f"Shortest Path: {start}  →  {end}   (distance = {total_dist})",
            start_node=start,
            end_node=end,
        )
        st.pyplot(fig)
        plt.close(fig)

    else:
        # Default: show the full map without highlighting
        st.markdown("### 🖼️ Full Campus Map")
        st.markdown(
            "<div class='info-banner'>👈  Select your locations in the sidebar "
            "and click <b>Find Shortest Path</b> to compute a route.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        fig = draw_campus_graph(
            edges=EDGES,
            title="DIU Campus — Full Map (no path selected)",
        )
        st.pyplot(fig)
        plt.close(fig)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — Step-by-Step Animation
# ─────────────────────────────────────────────────────────────────────────────
with tab_anim:
    st.markdown("### 🎬 Step-by-Step Path Animation")

    if "path" not in st.session_state:
        st.markdown(
            "<div class='info-banner'>👈  Find a path first (Graph & Path tab) "
            "to unlock the animation.</div>",
            unsafe_allow_html=True,
        )
    else:
        path  = st.session_state["path"]
        start = st.session_state["start"]
        end   = st.session_state["end"]
        dist  = st.session_state["dist"]
        speed = st.session_state.get("anim_speed", 0.8)

        st.markdown(
            f"<p style='color:#90CAF9;'>"
            f"<b>Route:</b> {start} → {end} &nbsp;|&nbsp; "
            f"<b>Distance:</b> {dist} units &nbsp;|&nbsp; "
            f"<b>Steps:</b> {len(path)}</p>",
            unsafe_allow_html=True,
        )

        play_btn = st.button("▶️  Play Animation", use_container_width=True, type="primary")

        if play_btn:
            animate_path(path, delay=speed, start_node=start, end_node=end)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — Distance Table
# ─────────────────────────────────────────────────────────────────────────────
with tab_table:
    st.markdown("### 📋 All Distances from Start Node")

    if "distances" not in st.session_state:
        st.markdown(
            "<div class='info-banner'>👈  Find a path first to populate "
            "the distance table.</div>",
            unsafe_allow_html=True,
        )
    else:
        start     = st.session_state["start"]
        distances = st.session_state["distances"]
        path_set  = set(st.session_state["path"])

        st.markdown(
            f"<p style='color:#90CAF9;'>Showing shortest distances "
            f"from <b>{start}</b> to every reachable campus location.</p>",
            unsafe_allow_html=True,
        )

        rows = []
        for node, d in sorted(distances.items(), key=lambda x: x[1]):
            rows.append({
                "Destination":     node,
                "Distance (units)": d if d != math.inf else "∞",
                "On Shortest Path": "🟢 Yes" if node in path_set else "—",
                "Reachable":        "✅" if d != math.inf else "❌",
            })

        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)
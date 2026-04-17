# visualization/animation.py
# ─────────────────────────────────────────────────────────────────────────────
# Step-by-step path animation using st.empty() + time.sleep()
# ─────────────────────────────────────────────────────────────────────────────
import time
import matplotlib.pyplot as plt
import streamlit as st

from visualization.graph_plot import draw_campus_graph
from graph.graph_data          import EDGES


def animate_path(path, delay=0.8, start_node=None, end_node=None):
    """
    Animate the shortest path step-by-step inside the Streamlit UI.

    Each frame:
    - Reveals one additional node of the path.
    - Colours the current node orange-red.
    - Colours already-visited path nodes green.
    - Displays a status bar with the current step.

    Parameters
    ----------
    path       : list[str]  Ordered nodes on the shortest path.
    delay      : float      Seconds to pause between frames.
    start_node : str        Source node (for colour differentiation).
    end_node   : str        Destination node (for colour differentiation).
    """
    if not path or len(path) < 2:
        st.warning("⚠️ Path is too short or empty — nothing to animate.")
        return

    # ── Persistent UI slots ───────────────────────────────────────────────────
    progress_bar   = st.progress(0)
    status_box     = st.empty()
    graph_slot     = st.empty()

    revealed = set()
    total    = len(path)

    for step_idx, node in enumerate(path):
        revealed.add(node)

        # Progress bar (0.0 → 1.0)
        progress_bar.progress((step_idx + 1) / total)

        # Status message
        status_box.markdown(
            f"""
            <div style="
                background: #1A1A2E;
                border-left: 4px solid #FF6D00;
                border-radius: 6px;
                padding: 10px 16px;
                color: #FFD700;
                font-size: 15px;
                font-weight: bold;
            ">
                🚶 Step {step_idx + 1} / {total} &nbsp;&nbsp;|&nbsp;&nbsp;
                Visiting: <span style="color:#FF6D00">{node}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Draw the frame
        fig = draw_campus_graph(
            edges=EDGES,
            path=path,
            highlight_nodes=revealed,
            title=f"Step {step_idx + 1} / {total}  —  Visiting: {node}",
            current_step_node=node,
            start_node=start_node,
            end_node=end_node,
        )
        graph_slot.pyplot(fig)
        plt.close(fig)

        time.sleep(delay)

    # ── Final frame: full path highlighted, no active node ───────────────────
    progress_bar.progress(1.0)

    fig = draw_campus_graph(
        edges=EDGES,
        path=path,
        highlight_nodes=set(path),
        title="✅  Shortest Path Animation Complete",
        current_step_node=None,
        start_node=start_node,
        end_node=end_node,
    )
    graph_slot.pyplot(fig)
    plt.close(fig)

    status_box.markdown(
        """
        <div style="
            background: #1A1A2E;
            border-left: 4px solid #00E676;
            border-radius: 6px;
            padding: 10px 16px;
            color: #00E676;
            font-size: 15px;
            font-weight: bold;
        ">
            ✅ Animation complete — shortest path fully traced!
        </div>
        """,
        unsafe_allow_html=True,
    )
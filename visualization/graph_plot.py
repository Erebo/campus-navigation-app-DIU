# visualization/graph_plot.py
# ─────────────────────────────────────────────────────────────────────────────
# Campus graph visualisation using NetworkX + Matplotlib
# ─────────────────────────────────────────────────────────────────────────────
import networkx as nx
import matplotlib
matplotlib.use("Agg")          # Non-interactive backend — required for Streamlit
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

from graph.graph_data import NODE_POSITIONS


# ── Colour palette ────────────────────────────────────────────────────────────
BG_COLOR          = "#0F0F1E"
NODE_DEFAULT      = "#4FC3F7"   # sky-blue  — regular node
NODE_PATH         = "#00E676"   # green     — node on shortest path
NODE_CURRENT      = "#FF6D00"   # orange    — node being animated right now
NODE_START        = "#FFD600"   # yellow    — start node
NODE_END          = "#FF1744"   # red       — end / destination node
EDGE_DEFAULT      = "#3A3A5C"   # dim indigo
EDGE_PATH         = "#FFD700"   # gold      — path edge highlight
LABEL_COLOR       = "#FFFFFF"
WEIGHT_COLOR      = "#90CAF9"


def build_nx_graph(edges):
    """Create an undirected weighted NetworkX graph from an edge list."""
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    return G


def draw_campus_graph(
    edges,
    path=None,
    highlight_nodes=None,
    title="DIU Campus Navigation",
    figsize=(20, 13),
    current_step_node=None,
    start_node=None,
    end_node=None,
):
    """
    Draw the full campus graph, optionally highlighting a shortest path.

    Parameters
    ----------
    edges             : list[(u, v, weight)]
    path              : list[str]  – ordered path nodes (optional)
    highlight_nodes   : set[str]   – nodes revealed so far (for animation)
    title             : str
    figsize           : tuple
    current_step_node : str        – node highlighted as 'current' in animation
    start_node        : str        – source node (yellow)
    end_node          : str        – destination node (red)

    Returns
    -------
    fig : matplotlib.figure.Figure
    """
    G   = build_nx_graph(edges)
    pos = {n: NODE_POSITIONS[n] for n in G.nodes() if n in NODE_POSITIONS}

    # ── Build path-edge set ───────────────────────────────────────────────────
    path_edge_set = set()
    if path and len(path) > 1:
        for i in range(len(path) - 1):
            path_edge_set.add((path[i], path[i + 1]))
            path_edge_set.add((path[i + 1], path[i]))

    # ── Partition edges ───────────────────────────────────────────────────────
    normal_edges = [
        (u, v) for u, v in G.edges()
        if (u, v) not in path_edge_set
    ]
    highlighted_edges = [
        (u, v) for u, v in G.edges()
        if (u, v) in path_edge_set
    ]

    # ── Assign node colours ───────────────────────────────────────────────────
    path_set = set(path) if path else set()
    revealed = highlight_nodes if highlight_nodes else set()

    def node_color(n):
        if n == current_step_node:
            return NODE_CURRENT
        if n == start_node:
            return NODE_START
        if n == end_node:
            return NODE_END
        if n in revealed and n in path_set:
            return NODE_PATH
        if n in path_set:
            return NODE_PATH
        return NODE_DEFAULT

    node_colors = [node_color(n) for n in G.nodes()]
    node_sizes  = [
        700 if n == current_step_node else
        550 if n in (start_node, end_node) else
        420 if n in path_set else
        260
        for n in G.nodes()
    ]

    # ── Figure setup ──────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")

    # ── Draw normal edges ─────────────────────────────────────────────────────
    nx.draw_networkx_edges(
        G, pos,
        edgelist=normal_edges,
        edge_color=EDGE_DEFAULT,
        width=1.4,
        alpha=0.65,
        ax=ax,
    )

    # ── Draw path edges (gold, thick) ─────────────────────────────────────────
    if highlighted_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=highlighted_edges,
            edge_color=EDGE_PATH,
            width=4.5,
            alpha=1.0,
            ax=ax,
            style="solid",
        )

    # ── Draw nodes ────────────────────────────────────────────────────────────
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=node_sizes,
        edgecolors="#FFFFFF",
        linewidths=0.6,
        ax=ax,
    )

    # ── Draw node labels ──────────────────────────────────────────────────────
    nx.draw_networkx_labels(
        G, pos,
        font_size=5.5,
        font_color=LABEL_COLOR,
        font_weight="bold",
        ax=ax,
    )

    # ── Draw edge weight labels ───────────────────────────────────────────────
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_size=5,
        font_color=WEIGHT_COLOR,
        bbox=dict(boxstyle="round,pad=0.1", fc=BG_COLOR, alpha=0.5, ec="none"),
        ax=ax,
    )

    # ── Legend ────────────────────────────────────────────────────────────────
    legend_entries = [
        mpatches.Patch(color=NODE_DEFAULT,  label="Campus Location"),
        mpatches.Patch(color=NODE_PATH,     label="On Shortest Path"),
        mpatches.Patch(color=NODE_START,    label="Start"),
        mpatches.Patch(color=NODE_END,      label="Destination"),
        mpatches.Patch(color=NODE_CURRENT,  label="Currently Visiting"),
        mpatches.Patch(color=EDGE_PATH,     label="Path Edge"),
    ]
    legend = ax.legend(
        handles=legend_entries,
        loc="lower left",
        framealpha=0.35,
        facecolor="#1A1A2E",
        edgecolor="#4FC3F7",
        labelcolor="white",
        fontsize=8,
    )

    ax.set_title(title, color="white", fontsize=13, fontweight="bold", pad=14)
    plt.tight_layout(pad=1.5)
    return fig
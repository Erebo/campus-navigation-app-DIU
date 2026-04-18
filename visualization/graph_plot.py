# visualization/graph_plot.py
# ─────────────────────────────────────────────────────────────────────────────
# Campus graph visualisation using NetworkX + Matplotlib
# ─────────────────────────────────────────────────────────────────────────────
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

from graph.graph_data import NODE_POSITIONS


# ── Colour palette ────────────────────────────────────────────────────────────
BG_COLOR          = "#0F0F1E"
NODE_DEFAULT      = "#4FC3F7"
NODE_PATH         = "#00E676"
NODE_CURRENT      = "#FF6D00"
NODE_START        = "#FFD600"
NODE_END          = "#FF1744"
EDGE_DEFAULT      = "#3A3A5C"
EDGE_PATH         = "#FFD700"
LABEL_COLOR       = "#FFFFFF"
WEIGHT_COLOR      = "#90CAF9"


def build_nx_graph(edges):
    G = nx.Graph()
    for u, v, w, dir_go, dir_return in edges:
        edge_label = f"{w}"   # cleaner (removed directions clutter)
        G.add_edge(u, v, weight=w, label=edge_label)
    return G


def draw_campus_graph(
    edges,
    path=None,
    highlight_nodes=None,
    title="DIU Campus Navigation",
    figsize=(14, 9),
    current_step_node=None,
    start_node=None,
    end_node=None,
):

    G = build_nx_graph(edges)
    pos = {n: NODE_POSITIONS[n] for n in G.nodes() if n in NODE_POSITIONS}

# 🔥 ADD THIS RIGHT BELOW
    scale = 2.2
    pos = {k: (x * scale, y * scale) for k, (x, y) in pos.items()}

    # ── Path edges ────────────────────────────────────────────────────────────
    path_edge_set = set()
    if path and len(path) > 1:
        for i in range(len(path) - 1):
            path_edge_set.add((path[i], path[i + 1]))
            path_edge_set.add((path[i + 1], path[i]))

    normal_edges = [(u, v) for u, v in G.edges() if (u, v) not in path_edge_set]
    highlighted_edges = [(u, v) for u, v in G.edges() if (u, v) in path_edge_set]

    # ── Node styling ──────────────────────────────────────────────────────────
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
        1100 if n == current_step_node else
        900 if n in (start_node, end_node) else
        700 if n in path_set else
        500
        for n in G.nodes()
    ]

    # ── Figure setup ──────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")

    # ── Edges ─────────────────────────────────────────────────────────────────
    nx.draw_networkx_edges(
        G, pos,
        edgelist=normal_edges,
        edge_color="#6A6AFF",
        width=3.0,
        alpha=0.9,
        ax=ax,
    )

    if highlighted_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=highlighted_edges,
            edge_color="#00E676",   # neon green
            width=6.0,              # thicker
            alpha=1.0,
            ax=ax,
)

    # ── Nodes ─────────────────────────────────────────────────────────────────
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=node_sizes,
        edgecolors="#FFFFFF",
        linewidths=0.8,
        ax=ax,
    )

    # ── Labels (FIXED + OUTLINE) ──────────────────────────────────────────────
    labels = nx.draw_networkx_labels(
        G, pos,
        font_size=10,
        font_color=LABEL_COLOR,
        font_weight="bold",
        ax=ax
    )

    if labels:
        for text in labels.values():
            text.set_path_effects([
                pe.Stroke(linewidth=2.5, foreground='black'),
                pe.Normal()
            ])

    # ── Edge labels (optional – can disable if cluttered) ─────────────────────
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_size=6,
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
        mpatches.Patch(color=NODE_CURRENT,  label="Current Node"),
        mpatches.Patch(color=EDGE_PATH,     label="Path Edge"),
    ]

    ax.legend(
        handles=legend_entries,
        loc="lower left",
        framealpha=0.35,
        facecolor="#1A1A2E",
        edgecolor="#4FC3F7",
        labelcolor="white",
        fontsize=8,
    )

    # ── Title ─────────────────────────────────────────────────────────────────
    ax.set_title(title, color="white", fontsize=13, fontweight="bold", pad=14)

    plt.tight_layout(pad=1.2)
    return fig
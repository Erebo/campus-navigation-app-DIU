# graph/path_utils.py
# ─────────────────────────────────────────────────────────────────────────────
# Path reconstruction helpers
# ─────────────────────────────────────────────────────────────────────────────
import math


def reconstruct_path(previous, start, end):
    """
    Walk backwards through the `previous` dict to build the
    ordered path from `start` → `end`.

    Parameters
    ----------
    previous : dict   {node: predecessor}  from dijkstra()
    start    : str    source node
    end      : str    destination node

    Returns
    -------
    path : list[str]
        Ordered list of nodes from start to end.
        Returns an empty list if no path exists.
    """
    path    = []
    current = end

    # Trace back from end to start
    while current is not None:
        path.append(current)
        current = previous.get(current)

    path.reverse()

    # Validate: path must begin at start
    if not path or path[0] != start:
        return []

    return path


def format_path(path):
    """
    Return a human-readable arrow string.

    Example
    -------
    >>> format_path(["Main Gate 1", "DIU Transport Hub", "Bike Garage"])
    'Main Gate 1 → DIU Transport Hub → Bike Garage'
    """
    return " → ".join(path)


def path_total_distance(distances, end):
    """
    Return the total distance to `end` from the dijkstra distances dict.
    Returns '∞' if unreachable.
    """
    d = distances.get(end, math.inf)
    return d if d != math.inf else "∞"
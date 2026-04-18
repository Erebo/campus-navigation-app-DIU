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

def get_turn_by_turn_directions(path, graph):
    """
    Generates human-readable compass directions for the UI.

    Parameters
    ----------
    path : list[str]
        Ordered list of nodes from start to end (from reconstruct_path)
    graph : dict
        The main adjacency dictionary containing the direction strings.

    Returns
    -------
    list[str]
        A list of formatted instructional strings.
    """
    if not path:
        return []
        
    if len(path) == 1:
        return ["You are already at your destination!"]

    directions = []
    
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        
        # Look up the compass direction stored in the graph
        compass_dir = graph[current_node][next_node]['direction']
        
        # Format the step beautifully
        step = f"Walk {compass_dir} towards {next_node}."
        directions.append(step)

    return directions
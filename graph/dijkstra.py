# graph/dijkstra.py
# ─────────────────────────────────────────────────────────────────────────────
# Dijkstra's Algorithm  —  O((V + E) log V)  via min-heap
# ─────────────────────────────────────────────────────────────────────────────
import heapq
import math


def dijkstra(graph, start):
    """
    Compute shortest distances from `start` to every reachable node.

    Parameters
    ----------
    graph : dict
        Adjacency dict  {node: {neighbor: weight, ...}, ...}
    start : str
        Source node.

    Returns
    -------
    distances : dict
        {node: shortest_distance_from_start}
        Unreachable nodes keep their initial value of math.inf.
    previous : dict
        {node: predecessor_on_shortest_path}
        Used by path_utils.reconstruct_path() to walk the path back.
    """
    # Initialise all distances to infinity
    distances = {node: math.inf for node in graph}
    previous  = {node: None     for node in graph}
    distances[start] = 0

    # Min-heap entries: (cumulative_cost, node)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Stale entry — a shorter path was already found
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            tentative = current_dist + weight

            if tentative < distances[neighbor]:
                distances[neighbor] = tentative
                previous[neighbor]  = current_node
                heapq.heappush(heap, (tentative, neighbor))

    return distances, previous
# graph/graph_data.py
# ─────────────────────────────────────────────────────────────────────────────
# DIU CAMPUS NAVIGATION — Graph Data
# ─────────────────────────────────────────────────────────────────────────────

# ── NODES ────────────────────────────────────────────────────────────────────
NODES = [
    "Admission Office",
    "Bike Garage",
    "Boat Lake",
    "Bonomaya",
    "Bonomaya 2",
    "Central Jame Mosque",
    "Central Playground",
    "Department of Civil Engineering",
    "Department of EEE",
    "DIU Garden",
    "DIU Health and Fitness Center",
    "DIU Sports Dormitory",
    "DIU Transport Hub",
    "DIU Zoo",
    "Food Court",
    "Golf Yard",
    "Green Garden",
    "Inspiration Building",
    "Knowledge Tower",
    "LAB Academic Building",
    "Main Gate 1",
    "Main Gate 2",
    "Main Gate 3",
    "Main Gate 4",
    "Main Gate 5",
    "Main Gate 6",
    "Main Gate 7",
    "Main Gate 8",
    "Main Gate 9",
    "Nursery",
    "RASG 1",
    "RASG 2",
    "Shadhinota Shommelon Kendro",
    "Shaheed Minar",
    "Swimming Pool",
    "Volleyball Court",
    "YKSG 1",
    "YKSG 2",
]

# ── EDGES  (node1, node2, weight) ─────────────────────────────────────────────
# ⚠️  PLACEHOLDER distances — replace with real campus measurements.
#     Format: ("Location A", "Location B", distance_in_meters_or_units)
# ─────────────────────────────────────────────────────────────────────────────
EDGES = [
    # Main Gates → nearby hubs
    ("Main Gate 1",  "DIU Transport Hub",               2),
    ("Main Gate 1",  "Bike Garage",                     3),
    ("Main Gate 2",  "DIU Transport Hub",               3),
    ("Main Gate 2",  "LAB Academic Building",           4),
    ("Main Gate 3",  "LAB Academic Building",           3),
    ("Main Gate 3",  "Shaheed Minar",                   2),
    ("Main Gate 4",  "Shaheed Minar",                   2),
    ("Main Gate 4",  "Department of Civil Engineering", 3),
    ("Main Gate 5",  "Department of Civil Engineering", 2),
    ("Main Gate 5",  "Department of EEE",               3),
    ("Main Gate 6",  "Department of EEE",               2),
    ("Main Gate 6",  "Knowledge Tower",                 3),
    ("Main Gate 7",  "Knowledge Tower",                 2),
    ("Main Gate 7",  "Boat Lake",                       4),
    ("Main Gate 8",  "Boat Lake",                       3),
    ("Main Gate 8",  "DIU Zoo",                         4),
    ("Main Gate 9",  "DIU Zoo",                         2),
    ("Main Gate 9",  "Swimming Pool",                   3),

    # Transport & entry zone
    ("DIU Transport Hub", "Bike Garage",                        2),
    ("DIU Transport Hub", "DIU Health and Fitness Center",      3),
    ("Bike Garage",       "Nursery",                            4),
    ("Bike Garage",       "RASG 1",                             5),

    # Southern residential zone
    ("Nursery",            "RASG 1",                            2),
    ("Nursery",            "RASG 2",                            2),
    ("Nursery",            "DIU Health and Fitness Center",     3),
    ("RASG 1",             "RASG 2",                            2),
    ("RASG 2",             "DIU Sports Dormitory",              4),
    ("DIU Sports Dormitory", "Golf Yard",                       3),
    ("DIU Sports Dormitory", "Volleyball Court",                3),
    ("DIU Sports Dormitory", "Bonomaya 2",                      4),

    # Academic core
    ("LAB Academic Building", "Admission Office",               3),
    ("LAB Academic Building", "Inspiration Building",           2),
    ("Admission Office",      "Shaheed Minar",                  2),
    ("Admission Office",      "Department of Civil Engineering",3),
    ("Shaheed Minar",         "Central Jame Mosque",            2),
    ("Shaheed Minar",         "Department of Civil Engineering",3),
    ("Department of Civil Engineering", "Central Jame Mosque",  2),
    ("Department of Civil Engineering", "Department of EEE",    3),
    ("Department of EEE",     "Shadhinota Shommelon Kendro",    2),
    ("Knowledge Tower",       "Shadhinota Shommelon Kendro",    3),
    ("Knowledge Tower",       "Boat Lake",                      5),

    # Central zone
    ("Central Jame Mosque", "Food Court",                       3),
    ("Central Jame Mosque", "Inspiration Building",             4),
    ("Inspiration Building","Food Court",                       2),
    ("Inspiration Building","DIU Health and Fitness Center",    3),
    ("Food Court",          "Central Playground",               2),
    ("Food Court",          "Bonomaya",                         3),
    ("Central Playground",  "Bonomaya 2",                       3),
    ("Central Playground",  "Volleyball Court",                 4),
    ("Bonomaya",            "Bonomaya 2",                       2),
    ("Bonomaya",            "Green Garden",                     3),

    # Eastern & garden zone
    ("Shadhinota Shommelon Kendro", "DIU Garden",               3),
    ("Shadhinota Shommelon Kendro", "Green Garden",             4),
    ("Green Garden",  "DIU Garden",                             2),
    ("Green Garden",  "Volleyball Court",                       3),
    ("DIU Garden",    "Boat Lake",                              3),
    ("DIU Garden",    "YKSG 1",                                 4),
    ("DIU Garden",    "Golf Yard",                              4),
    ("DIU Garden",    "DIU Zoo",                                4),

    # Recreation & sports east
    ("Volleyball Court", "Swimming Pool",                       4),
    ("Swimming Pool",    "DIU Zoo",                             3),
    ("Swimming Pool",    "Golf Yard",                           2),
    ("DIU Zoo",          "YKSG 1",                              3),
    ("DIU Zoo",          "YKSG 2",                              2),
    ("YKSG 1",           "YKSG 2",                              2),
    ("YKSG 2",           "Boat Lake",                           3),

    # Bonomaya 2 connector
    ("Bonomaya 2",       "Central Playground",                  3),
]

# ── NODE POSITIONS  (x, y) for matplotlib layout ─────────────────────────────
# Roughly mirrors a real campus map. Adjust values to match actual layout.
NODE_POSITIONS = {
    "Main Gate 1":                      (0.0,  5.0),
    "Main Gate 2":                      (1.0,  7.5),
    "Main Gate 3":                      (2.5,  9.5),
    "Main Gate 4":                      (4.0,  9.8),
    "Main Gate 5":                      (5.5,  9.5),
    "Main Gate 6":                      (7.0,  9.2),
    "Main Gate 7":                      (8.5,  8.2),
    "Main Gate 8":                      (9.5,  6.5),
    "Main Gate 9":                      (9.5,  4.0),
    "Admission Office":                 (3.0,  7.2),
    "Bike Garage":                      (0.5,  3.5),
    "Boat Lake":                        (8.5,  7.5),
    "Bonomaya":                         (5.0,  5.5),
    "Bonomaya 2":                       (4.5,  4.5),
    "Central Jame Mosque":              (4.0,  7.5),
    "Central Playground":               (4.0,  4.0),
    "Department of Civil Engineering":  (4.5,  8.2),
    "Department of EEE":                (5.5,  8.7),
    "DIU Garden":                       (7.0,  6.5),
    "DIU Health and Fitness Center":    (1.5,  4.5),
    "DIU Sports Dormitory":             (5.5,  2.5),
    "DIU Transport Hub":                (0.5,  5.5),
    "DIU Zoo":                          (9.0,  5.0),
    "Food Court":                       (4.0,  6.2),
    "Golf Yard":                        (7.5,  3.2),
    "Green Garden":                     (6.0,  5.2),
    "Inspiration Building":             (2.5,  5.8),
    "Knowledge Tower":                  (6.5,  8.7),
    "LAB Academic Building":            (2.0,  7.2),
    "Nursery":                          (1.5,  2.5),
    "RASG 1":                           (0.5,  1.5),
    "RASG 2":                           (2.0,  1.5),
    "Shadhinota Shommelon Kendro":      (6.0,  7.5),
    "Shaheed Minar":                    (3.5,  8.5),
    "Swimming Pool":                    (8.5,  4.0),
    "Volleyball Court":                 (6.0,  4.0),
    "YKSG 1":                           (8.5,  6.0),
    "YKSG 2":                           (9.0,  7.0),
}


# ── Graph builder ─────────────────────────────────────────────────────────────
def build_graph(edges):
    """
    Build an undirected weighted adjacency dictionary from an edge list.

    Parameters
    ----------
    edges : list of (str, str, int|float)

    Returns
    -------
    graph : dict  {node: {neighbor: weight, ...}, ...}
    """
    graph = {node: {} for node in NODES}
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w
    return graph


# Pre-built graph ready to import
GRAPH = build_graph(EDGES)
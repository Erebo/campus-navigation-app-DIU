# graph/graph_data.py
# ─────────────────────────────────────────────────────────────────────────────
# DIU CAMPUS NAVIGATION — Graph Data
# ─────────────────────────────────────────────────────────────────────────────

# ── NODES ────────────────────────────────────────────────────────────────────
NODES = [
    "Admission Office", "Bike Garage", "Boat Lake", "Bonomaya", "Bonomaya 2",
    "Central Jame Mosque", "Department of Civil Engineering",
    "Department of EEE", "DIU Garden", "DIU Health and Fitness Center",
    "DIU Sports Dorm", "DIU Transport Hub", "DIU Zoo", "Food Court",
    "Golf Yard", "Green Garden", "Inspiration Building", "Knowledge Tower",
    "LAB Academic Building", "Main Gate 1", "Main Gate 2", "Main Gate 3",
    "Main Gate 4", "Main Gate 5", "Main Gate 6", "Main Gate 7", "Main Gate 8",
    "Main Gate 9", "Nursery", "RASG 1", "RASG 2", "Shadhinota Shommelon Kendro",
    "Shaheed Minar", "Kathal Tola", "Volleyball Court", "YKSG 1", "YKSG 2", "DIU Logo",
]

# ── EDGES  (node1, node2, weight, direction_1_to_2, direction_2_to_1) ─────────
# Weight is now set to estimated distance in meters!
# ─────────────────────────────────────────────────────────────────────────────
EDGES = [
    ("Admission Office", "Shaheed Minar", 20, "West", "East"),
    ("Admission Office", "Volleyball Court", 15, "East", "West"),
    ("Volleyball Court", "Green Garden", 15, "East", "West"),
    
    ("Knowledge Tower", "Kathal Tola", 25, "South", "North"),
    ("Knowledge Tower", "Bike Garage", 30, "North", "South"),
    ("Bike Garage", "Shadhinota Shommelon Kendro", 30, "North-East", "South-West"),
    ("Bike Garage", "RASG 2", 35, "North", "South"),
    ("RASG 2", "Shadhinota Shommelon Kendro", 20, "East", "West"),
    ("Green Garden", "LAB Academic Building", 20, "North-East", "South-West"),
    ("LAB Academic Building", "Central Jame Mosque", 15, "North-West", "South-East"),
    ("Central Jame Mosque", "Inspiration Building", 20, "North", "South"),
   
    ("Inspiration Building", "DIU Transport Hub", 25, "East", "West"),
   
    ("Inspiration Building", "Nursery", 25, "North-West", "South-East"),
    ("Inspiration Building", "Bonomaya", 25, "North", "South"),
    ("Nursery", "Food Court", 20, "North", "South"),
    ("Food Court", "Bonomaya", 15, "East", "West"),
    ("Bonomaya", "DIU Garden", 20, "North", "South"),
    ("DIU Health and Fitness Center", "Food Court", 15, "South", "North"),
    ("DIU Sports Dorm", "Shadhinota Shommelon Kendro", 15, "South", "North"),
    ("DIU Zoo", "RASG 1", 20, "East", "West"),
    ("DIU Health and Fitness Center", "Boat Lake", 25, "North", "South"),
    ("DIU Health and Fitness Center", "RASG 1", 30, "East", "West"),
    ("DIU Garden", "DIU Health and Fitness Center", 20, "West", "East"),
    ("RASG 1", "Bonomaya 2", 25, "South-East", "North-West"),
    ("DIU Zoo", "Bonomaya 2", 20, "South", "North"),
    ("Boat Lake", "Main Gate 7", 30, "North", "South"),
    ("Main Gate 7", "Department of EEE", 40, "North-West", "South-East"),
    ("Department of EEE", "Department of Civil Engineering", 35, "North", "South"),
    ("Golf Yard", "Shaheed Minar", 25, "East", "West"),
    ("Golf Yard", "Kathal Tola", 20, "North", "South"),
    ("Main Gate 1", "Admission Office", 15, "North", "South"),
    ("Main Gate 2", "Admission Office", 15, "North", "South"),
    ("Main Gate 3", "Green Garden", 15, "North", "South"),
    ("Main Gate 4", "Knowledge Tower", 15, "East", "West"),
    ("Main Gate 5", "Bike Garage", 15, "East", "West"),
    ("Main Gate 6", "Shadhinota Shommelon Kendro", 20, "South", "North"),
    ("Main Gate 7", "YKSG 2", 25, "East", "West"),
    ("Main Gate 8", "Main Gate 9", 25, "North-East", "South-West"),
    ("Main Gate 8", "YKSG 1", 30, "South", "North"),
    ("Bonomaya 2", "Main Gate 9", 25, "South", "North"),
    ("DIU Transport Hub", "Main Gate 8", 35, "East", "West"),
    ("Main Gate 6", "Boat Lake", 15, "North-East", "South-West"),
    ("DIU Logo", "Knowledge Tower", 25, "West", "East"),
    ("DIU Logo", "Shadhinota Shommelon Kendro", 35, "North", "South"),
    ("DIU Logo", "Inspiration Building", 45, "East", "West"),
]

# ── NODE POSITIONS  (x, y) for matplotlib layout ─────────────────────────────
# Updated to perfectly match the diagrams.net spatial layout
NODE_POSITIONS = {
    # ── Top Section ──
    "Department of Civil Engineering":  (5.0, 15.0),
    "Department of EEE":                (5.0, 13.5),
    "Main Gate 7":                      (4.5, 12.0),
    "YKSG 2":                           (6.5, 12.0),
    "Boat Lake":                        (5.0, 10.5),

    # ── Upper Middle Section ──
    "DIU Sports Dorm":                  (2.5,  11.0),
    "Main Gate 6":                      (3.5,  9.5),
    "DIU Health and Fitness Center":    (4.5,  9.0),
    "RASG 1":                           (6.5,  9.5),
    "DIU Zoo":                          (8.0,  9.5),

    # ── Middle Section ──
    "RASG 2":                           (1.0,  8.0),
    "Shadhinota Shommelon Kendro":      (3.0,  8.0),
    "Food Court":                       (4.5,  8.0),
    "DIU Garden":                       (6.5,  8.0),
    "Bonomaya 2":                       (8.5,  8.0),

    # ── Lower Middle Section ──
    "Main Gate 5":                      (0.0,  7.5),
    "Bike Garage":                      (1.5,  6.5),
    "Nursery":                          (4.5,  6.5),
    "Bonomaya":                         (6.5,  6.5),
    "Main Gate 9":                      (9.5,  7.0),

    # ── Lower Section ──
    "Main Gate 4":                      (0.0,  5.0),
    "Knowledge Tower":                  (1.5,  5.0),
    "DIU Logo":                         (3.0,  5.0),

    "Inspiration Building":             (6.5,  5.0),
    "Main Gate 8":                      (8.5,  6.0),
    "DIU Transport Hub":                (8.0,  4.0),
    "YKSG 1":                           (10.0, 4.0),

    # ── Bottom Section ──
    "Kathal Tola":                      (1.5,  3.5),
    "Golf Yard":                        (1.5,  2.0),
    "Shaheed Minar":                    (3.0,  1.5),
    "Admission Office":                 (4.0,  1.0),
    "Volleyball Court":                 (5.5,  1.5),
    "Green Garden":                     (6.5,  1.5),
    "Central Jame Mosque":              (6.5,  3.5),
    "LAB Academic Building":            (7.0,  2.5),

    # ── Bottom Gates ──
    "Main Gate 1":                      (3.5,  0.0),
    "Main Gate 2":                      (4.5,  0.0),
    "Main Gate 3":                      (6.0,  0.0),
}


# ── Graph builder ─────────────────────────────────────────────────────────────
def build_graph(edges):
    """
    Build an undirected weighted adjacency dictionary from an edge list.
    Now includes hardcoded compass directions!
    """
    graph = {node: {} for node in NODES}
    
    for u, v, w, dir_u_to_v, dir_v_to_u in edges:
        # Save the weight AND the compass direction as a dictionary
        graph[u][v] = {'weight': w, 'direction': dir_u_to_v}
        graph[v][u] = {'weight': w, 'direction': dir_v_to_u}
        
    return graph

# Pre-built graph ready to import
GRAPH = build_graph(EDGES)
# 🎓 DIU Campus Navigation System

A graph-based campus navigation application that computes and visualizes the shortest path between locations using **Dijkstra’s Algorithm** 🚀

This project was developed as part of the **CSE 213 (Data Structures & Algorithms)** course.

---
## 🌐 Live Demo

You can access the deployed application here:

👉 https://diu-campus-navigator.streamlit.app/

---

## 🚀 Try It Online

* Select a start location
* Choose a destination
* Click **Find Shortest Path**
* Explore graph, animation, and distance table

No installation required — runs directly in your browser.


## 📌 Project Overview

This system models the DIU campus as a **weighted graph**, where:

* 📍 Nodes represent campus locations
* 🔗 Edges represent paths between locations
* 📏 Weights represent distances

The application allows users to compute the **shortest route** and visualize it interactively.

---

## ✨ Features

* 🔍 Shortest path computation using Dijkstra’s Algorithm
* 📊 Graph-based campus visualization
* 🎬 Step-by-step path animation
* 📋 Distance table from source node
* 🎯 Highlighted optimal route
* 🎨 Clean and modern Streamlit UI

---

## 🧠 Graph Representation

The campus is represented as:

G = (V, E)

* V → Locations (nodes)
* E → Connections (edges)

Each edge has a weight representing distance.

---

## ⚙️ Algorithm Used

### 🟢 Dijkstra’s Algorithm

Computes the shortest path from a source node to all other nodes.

#### 🔄 Steps:

1. Initialize all distances as ∞
2. Set source distance = 0
3. Use a min-heap (priority queue)
4. Select nearest node
5. Update neighbors
6. Repeat

#### ⏱️ Time Complexity:

O((V + E) log V)

---

## ❓ Why Not DFS or BFS?

* 🔴 **DFS (Depth First Search)**
  Does not consider weights → ❌ Not suitable

* 🟡 **BFS (Breadth First Search)**
  Works only for equal weights → ⚠️ Limited

* 🟢 **Dijkstra’s Algorithm**
  Handles weighted graphs → ✅ Best choice

---

## 🗂️ Project Structure

```id="k0fy2g"
campus-navigation-app-DIU/
│
├── app.py                     # Main Streamlit app
│
├── graph/
│   ├── __init__.py
│   ├── graph_data.py          # Nodes, edges, positions
│   ├── dijkstra.py            # Algorithm
│   ├── path_utils.py          # Path utilities
│
├── visualization/
│   ├── __init__.py
│   ├── graph_plot.py          # Graph drawing
│   ├── animation.py           # Animation
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```id="y6pntx"
git clone https://github.com/your-username/campus-navigation-app-DIU.git
cd campus-navigation-app-DIU
```

---

### 2️⃣ Create virtual environment

```id="rzn6bj"
py -3.11 -m venv venv
venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install dependencies

```id="fxzmgv"
pip install -r requirements.txt
```

---

### 4️⃣ Run the application

```id="b2dy3j"
streamlit run app.py
```

---

## 🖥️ Usage

1. 📍 Select Start Location
2. 🏁 Select Destination
3. 🔍 Click "Find Shortest Path"
4. Explore:

   * 📊 Graph & Path
   * 🎬 Animation
   * 📋 Distance Table

---

## 📊 Example Output

```id="u0nbc1"
Main Gate 2 → LAB Academic Building → Shaheed Minar → Central Jame Mosque
```

---

## 🧪 Technologies Used

* 🐍 Python
* 🌐 Streamlit
* 📊 NetworkX
* 📈 Matplotlib
* 🧮 Pandas

---

## 🎓 Academic Context

📘 Course: **CSE 213 — Algorithms**

Concepts covered:

* Graph data structure
* Weighted graphs
* Shortest path algorithms
* Algorithm visualization

---

## 🚀 Future Improvements

* 🗺️ Real campus map integration
* 📍 GPS-based navigation
* 🔎 Interactive zoomable map
* 📱 Mobile-friendly UI
* 🔄 Dynamic real-time updates

---

## 👨‍💻 Authors :

**Mahadi Rahman Jihad**
**Tartib Kaiser Munna**
**Tasfia Mozumder Aupy**
**Tahseen Alam**
**Aminul Islam Rimon**

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgment

This project demonstrates the practical application of graph algorithms in real-world navigation systems, using a model derived from the original map of Daffodil International University

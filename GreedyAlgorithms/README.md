# 📂 `GreedyAlgorithms/README.md`

## 📑 Table of Contents

1. [Activity Selection](#1-activity-selection)
2. [Huffman Coding](#2-huffman-coding)
3. [Job Sequencing with Deadlines](#3-job-sequencing-with-deadlines)
4. [Minimum Spanning Tree (Prim’s & Kruskal’s)](#4-minimum-spanning-tree-prims--kruskals)
5. [Greedy Shortest Path (Dijkstra’s Algorithm)](#5-greedy-shortest-path-dijkstras-algorithm)

---

## 🔹 1. Activity Selection

**Explanation:**
Given activities with start & finish times, select the maximum number of non-overlapping activities.
Greedy choice → pick the activity that finishes earliest.

**Pseudocode:**

```
procedure activity_selection(activities):
    sort activities by finish time
    last_finish = -∞
    result = []
    for (s, f) in activities:
        if s >= last_finish:
            result.append((s, f))
            last_finish = f
    return result
```

**Complexity:**

* Time: O(n log n) (sorting)
* Space: O(1).

---

## 🔹 2. Huffman Coding

**Explanation:**
Used for lossless data compression. Build a binary tree where:

* Least frequent characters have longest codes.
* Frequent characters have shorter codes.

**Steps:**

1. Count frequency of characters.
2. Build a min-heap of nodes.
3. Extract 2 smallest, merge them, push back.
4. Repeat until heap has 1 node (root of Huffman tree).

**Pseudocode:**

```
procedure huffman(frequencies):
    create min_heap from frequencies
    while heap size > 1:
        left = extract_min(heap)
        right = extract_min(heap)
        merged = new_node(left.freq+right.freq, left, right)
        insert(heap, merged)
    return heap[0]  // root
```

**Complexity:**

* Time: O(n log n)
* Space: O(n).

---

## 🔹 3. Job Sequencing with Deadlines

**Explanation:**
Jobs have profits & deadlines. Goal: maximize profit within deadlines.
Greedy choice → schedule jobs with higher profit first.

**Pseudocode:**

```
procedure job_sequencing(jobs):
    sort jobs by profit (descending)
    result = [None]*max_deadline
    total_profit = 0
    for job in jobs:
        for t=job.deadline-1 down to 0:
            if result[t] == None:
                result[t] = job.id
                total_profit += job.profit
                break
    return (result, total_profit)
```

**Complexity:**

* Time: O(n²) (or O(n log n) with DSU optimization).
* Space: O(n).

---

## 🔹 4. Minimum Spanning Tree (Prim’s & Kruskal’s)

### **Prim’s Algorithm**

* Start with one vertex, expand MST by adding min weight edge connecting visited ↔ unvisited.

**Pseudocode:**

```
procedure prim(graph):
    mst = []
    visited = set()
    pq = min_heap(edges from start node)
    while pq:
        (w,u,v) = extract_min(pq)
        if v not in visited:
            visited.add(v)
            mst.append((u,v,w))
            push edges(v) to pq
    return mst
```

* Time: O(E log V)
* Space: O(V+E).

---

### **Kruskal’s Algorithm**

* Sort edges by weight, add if no cycle (using DSU).

**Pseudocode:**

```
procedure kruskal(graph):
    sort edges by weight
    ds = DisjointSet()
    mst = []
    for (u,v,w) in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u,v)
            mst.append((u,v,w))
    return mst
```

* Time: O(E log E)
* Space: O(V).

---

## 🔹 5. Greedy Shortest Path (Dijkstra’s Algorithm)

**Explanation:**
Find shortest path from source to all vertices (non-negative weights).

**Steps:**

1. Initialize distance\[source]=0, others=∞.
2. Use priority queue (min-heap).
3. Extract min distance node, relax neighbors.

**Pseudocode:**

```
procedure dijkstra(graph, source):
    dist = {v: ∞ for v in graph}
    dist[source] = 0
    pq = min_heap((0, source))
    while pq:
        (d,u) = extract_min(pq)
        for (v,w) in graph[u]:
            if d+w < dist[v]:
                dist[v] = d+w
                push(pq, (dist[v], v))
    return dist
```

**Complexity:**

* Time: O(E log V)
* Space: O(V+E).

---

## 📊 Comparison Table

| Algorithm                     | Use Case                       | Time               | Space  |
| ----------------------------- | ------------------------------ | ------------------ | ------ |
| Activity Selection            | Max non-overlapping activities | O(n log n)         | O(1)   |
| Huffman Coding                | Compression (prefix codes)     | O(n log n)         | O(n)   |
| Job Sequencing with Deadlines | Max profit scheduling          | O(n²) / O(n log n) | O(n)   |
| MST (Prim’s)                  | Minimum spanning tree          | O(E log V)         | O(V+E) |
| MST (Kruskal’s)               | Minimum spanning tree          | O(E log E)         | O(V)   |
| Dijkstra’s Algorithm          | Shortest path                  | O(E log V)         | O(V+E) |

---

## 📂 File Structure

```
GreedyAlgorithms/
├── activity_selection.py
├── huffman_coding.py
├── job_sequencing.py
├── prims.py
├── kruskals.py
├── dijkstra.py
└── README.md
```

---

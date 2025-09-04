# 📂 `AdvancedDSA/README.md`

## 📑 Table of Contents

1. [Union-Find / Disjoint Set (DSU)](#1-union-find--disjoint-set-dsu)
2. [Binary Indexed Tree (Fenwick Tree)](#2-binary-indexed-tree-fenwick-tree)
3. [Segment Tree](#3-segment-tree)
4. [String Matching Algorithms](#4-string-matching-algorithms)

   * [Knuth–Morris–Pratt (KMP)](#41-knuth–morris–pratt-kmp)
   * [Rabin-Karp](#42-rabin-karp)
   * [Z-Algorithm](#43-z-algorithm)

---

## 🔹 1. Union-Find / Disjoint Set (DSU)

**Explanation:**

* Data structure for keeping track of connected components.
* Supports two main operations:

  * `find(x)`: Find the representative of the set containing `x`.
  * `union(x, y)`: Merge sets containing `x` and `y`.
* Optimized with:

  * **Path Compression** → speeds up `find`.
  * **Union by Rank/Size** → balances the tree.

**Complexity:**

* Amortized O(α(N)) per operation (α = Inverse Ackermann, almost constant).

**Applications:**

* Kruskal’s MST, cycle detection, connected components.

---

## 🔹 2. Binary Indexed Tree (Fenwick Tree)

**Explanation:**

* Data structure to efficiently compute **prefix sums** and update elements.
* Useful for **range queries** like sum of elements from 1…i.

**Operations:**

* `update(i, val)` → O(log N)
* `prefix_sum(i)` → O(log N)
* `range_sum(l, r)` → prefix\_sum(r) – prefix\_sum(l-1)

**Complexity:**

* Time: O(log N) per query/update
* Space: O(N)

**Applications:**

* Range sum queries, inversion count, competitive programming.

---

## 🔹 3. Segment Tree

**Explanation:**

* Binary tree structure for answering **range queries** (sum, min, max, gcd, etc.).
* Supports both **query** and **update** in O(log N).

**Operations:**

* `build()` → O(N)
* `query(l, r)` → O(log N)
* `update(i, val)` → O(log N)

**Complexity:**

* Time: O(log N)
* Space: O(4N)

**Applications:**

* Range queries (sum, min, max), interval problems, RMQ.

---

## 🔹 4. String Matching Algorithms

### 4.1 Knuth–Morris–Pratt (KMP)

**Explanation:**

* Avoids re-checking characters using **LPS (Longest Prefix Suffix) array**.
* Preprocess pattern in O(m), search in O(n).

**Complexity:**

* Time: O(n + m)
* Space: O(m)

---

### 4.2 Rabin-Karp

**Explanation:**

* Uses **rolling hash** for substring search.
* Efficient for multiple pattern matching.

**Complexity:**

* Average: O(n + m)
* Worst: O(n·m) (hash collisions)

---

### 4.3 Z-Algorithm

**Explanation:**

* Builds **Z-array** where Z\[i] = length of longest substring starting at i that is also prefix of string.
* Used for pattern matching, string problems.

**Complexity:**

* Time: O(n + m)
* Space: O(n + m)

---

## 📊 Comparison Table

| Algorithm        | Use Case                            | Time       | Space  |
| ---------------- | ----------------------------------- | ---------- | ------ |
| Union-Find (DSU) | Connectivity, MST                   | \~O(1)     | O(N)   |
| Fenwick Tree     | Range sum, point update             | O(log N)   | O(N)   |
| Segment Tree     | Range queries, updates              | O(log N)   | O(N)   |
| KMP              | String matching                     | O(n+m)     | O(m)   |
| Rabin-Karp       | String matching (multiple patterns) | O(n+m) avg | O(1)   |
| Z-Algorithm      | String matching                     | O(n+m)     | O(n+m) |

---

## 📂 File Structure

```
AdvancedDSA/
├── union_find.py
├── fenwick_tree.py
├── segment_tree.py
├── kmp.py
├── rabin_karp.py
├── z_algorithm.py
└── README.md
```

---

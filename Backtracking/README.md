# 📂 `Backtracking/README.md`

## 📑 Table of Contents

1. [N-Queens Problem](#1-n-queens-problem)
2. [Sudoku Solver](#2-sudoku-solver)
3. [Rat in a Maze](#3-rat-in-a-maze)
4. [Word Search in a Grid](#4-word-search-in-a-grid)
5. [Generate All Subsets / Permutations](#5-generate-all-subsets--permutations)
6. [Palindrome Partitioning](#6-palindrome-partitioning)

---

## 🔹 1. N-Queens Problem

**Explanation:**

* Place N queens on an N×N chessboard such that no two queens attack each other.
* Use backtracking to try positions row by row, and backtrack when conflict arises.

**Complexity:**

* Time: O(N!)
* Space: O(N²)

**Applications:**

* Classic backtracking problem, demonstrates constraint satisfaction.

---

## 🔹 2. Sudoku Solver

**Explanation:**

* Fill 9×9 Sudoku board by placing numbers 1–9 while following Sudoku rules.
* Use backtracking + constraint checking.

**Complexity:**

* Time: O(9^(N\*N)) worst case
* Space: O(N²)

---

## 🔹 3. Rat in a Maze

**Explanation:**

* Rat starts at (0,0) and must reach (N-1,N-1) moving only allowed directions.
* Use DFS with backtracking to explore paths.

**Complexity:**

* Time: O(2^(N\*N)) worst case
* Space: O(N²)

---

## 🔹 4. Word Search in a Grid

**Explanation:**

* Given a 2D board and word, check if word exists in the grid by moving horizontally/vertically.
* Backtracking explores all possible paths.

**Complexity:**

* Time: O(N × M × 4^L)

  * N = rows, M = cols, L = word length
* Space: O(L)

---

## 🔹 5. Generate All Subsets / Permutations

* **Subsets:** Use recursion to include/exclude elements.
* **Permutations:** Swap elements recursively.

**Complexity:**

* Subsets: O(2^N)
* Permutations: O(N!)

---

## 🔹 6. Palindrome Partitioning

**Explanation:**

* Partition a string into all possible palindromic substrings.
* Backtrack by checking palindromes at each step.

**Complexity:**

* Time: O(2^N)
* Space: O(N)

---

## 📊 Comparison Table

| Problem                 | Time Complexity | Space Complexity | Notes               |
| ----------------------- | --------------- | ---------------- | ------------------- |
| N-Queens                | O(N!)           | O(N²)            | Classic CSP         |
| Sudoku Solver           | O(9^(N²))       | O(N²)            | Hard backtracking   |
| Rat in a Maze           | O(2^(N²))       | O(N²)            | Path finding        |
| Word Search             | O(N×M×4^L)      | O(L)             | Grid-based          |
| Subsets                 | O(2^N)          | O(N)             | Powerset generation |
| Permutations            | O(N!)           | O(N)             | Order matters       |
| Palindrome Partitioning | O(2^N)          | O(N)             | String-based        |

---

## 📂 File Structure

```
Backtracking/
├── n_queens.py
├── sudoku_solver.py
├── rat_in_maze.py
├── word_search.py
├── subsets.py
├── permutations.py
├── palindrome_partitioning.py
└── README.md
```

---

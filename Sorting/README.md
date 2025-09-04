# 🔄 Sorting Algorithms

This folder contains implementations of **fundamental, advanced, and hybrid sorting algorithms** in Python.  
Sorting is the process of arranging elements in a particular order (ascending/descending).  

---

## 📑 Table of Contents  

### 📘 Comparison-Based Sorts  
1. [Bubble Sort](#1-bubble-sort)  
2. [Selection Sort](#2-selection-sort)  
3. [Insertion Sort](#3-insertion-sort)  
4. [Merge Sort](#4-merge-sort)  
5. [Quick Sort](#5-quick-sort)  
6. [Heap Sort](#6-heap-sort)  
7. [Shell Sort](#7-shell-sort)  
8. [Comb Sort](#8-comb-sort)  
9. [Cycle Sort](#9-cycle-sort)  

### 🔢 Non-Comparison-Based Sorts  
10. [Counting Sort](#10-counting-sort)  
11. [Radix Sort](#11-radix-sort)  
12. [Bucket Sort](#12-bucket-sort)  
13. [Pigeonhole Sort](#13-pigeonhole-sort)  

### ⚡ Hybrid Sorts  
14. [Tim Sort](#14-tim-sort)  
15. [Intro Sort](#15-intro-sort)  

### 📊 Final Sections  
16. [Comparison Table](#-comparison-table)  
17. [File Structure](#-file-structure)  

---

## 📘 Algorithms Covered  

---

### 1. Bubble Sort (Comparison-Based)
**Explanation**: Repeatedly compares adjacent elements and swaps if out of order.  

⏱️ **Complexity**: Best O(n), Worst O(n²), Space O(1), Stable ✅  

---

### 2. Selection Sort (Comparison-Based)
**Explanation**: Repeatedly selects the minimum and places it at the beginning.  

⏱️ **Complexity**: Always O(n²), Space O(1), Stable ❌  

---

### 3. Insertion Sort (Comparison-Based)
**Explanation**: Inserts each element into its correct position within the sorted part.  

⏱️ **Complexity**: Best O(n), Worst O(n²), Space O(1), Stable ✅  

---

### 4. Merge Sort (Comparison-Based)
**Explanation**: Divide & Conquer → recursively split and merge.  

⏱️ **Complexity**: Always O(n log n), Space O(n), Stable ✅  

---

### 5. Quick Sort (Comparison-Based)
**Explanation**: Partition around pivot, recursively sort subarrays.  

⏱️ **Complexity**: Best O(n log n), Worst O(n²), Space O(log n), Stable ❌  

---

### 6. Heap Sort (Comparison-Based)
**Explanation**: Uses heap to repeatedly extract max.  

⏱️ **Complexity**: O(n log n), Space O(1), Stable ❌  

---

### 7. Shell Sort (Comparison-Based)
**Explanation**: Generalization of Insertion Sort using decreasing gap sequence.  

⏱️ **Complexity**: Best O(n log n), Worst O(n²), Space O(1), Stable ❌  

---

### 8. Comb Sort (Comparison-Based)
**Explanation**: Improves Bubble Sort using shrinking gap sequence (~1.3 factor).  

⏱️ **Complexity**: Best O(n log n), Worst O(n²), Space O(1), Stable ❌  

---

### 9. Cycle Sort (Comparison-Based)
**Explanation**: Places each element directly into its correct position by detecting cycles.  

⏱️ **Complexity**: Best/Worst O(n²), Space O(1), Stable ❌, Writes = O(n)  

---

### 10. Counting Sort (Non-Comparison-Based)
**Explanation**: Uses frequency counting for integers in a known range.  

⏱️ **Complexity**: O(n + k), Space O(n + k), Stable ✅  

---

### 11. Radix Sort (Non-Comparison-Based)
**Explanation**: Digit by digit sorting using Counting Sort.  

⏱️ **Complexity**: O(nk), Space O(n + k), Stable ✅  

---

### 12. Bucket Sort (Non-Comparison-Based)
**Explanation**: Distribute into buckets, sort each bucket, concatenate.  

⏱️ **Complexity**: Best O(n+k), Worst O(n²), Space O(n+k), Stable ✅  

---

### 13. Pigeonhole Sort (Non-Comparison-Based)
**Explanation**: Places items into pigeonholes based on values, reconstructs sorted list.  

⏱️ **Complexity**: O(n+range), Space O(range), Stable ✅  

---

### 14. Tim Sort (Hybrid)
**Explanation**: Python’s built-in sort → hybrid of Merge + Insertion Sort.  

⏱️ **Complexity**: Best O(n), Worst O(n log n), Space O(n), Stable ✅  

---

### 15. Intro Sort (Hybrid)
**Explanation**: C++ STL sort → hybrid of Quick + Heap + Insertion Sort.  

⏱️ **Complexity**: Best/Worst O(n log n), Space O(log n), Stable ❌  

---

## 📊 Comparison Table  

| Algorithm       | Type            | Best Case | Worst Case | Avg Case | Space | Stable | Notes |
|-----------------|-----------------|-----------|------------|----------|-------|--------|-------|
| Bubble Sort     | Comparison      | O(n)      | O(n²)      | O(n²)    | O(1)  | ✅     | Rarely used |
| Selection Sort  | Comparison      | O(n²)     | O(n²)      | O(n²)    | O(1)  | ❌     | Fewest swaps |
| Insertion Sort  | Comparison      | O(n)      | O(n²)      | O(n²)    | O(1)  | ✅     | Great for small/partial arrays |
| Merge Sort      | Comparison      | O(n log n)| O(n log n) | O(n log n)| O(n) | ✅     | Divide & Conquer |
| Quick Sort      | Comparison      | O(n log n)| O(n²)      | O(n log n)| O(log n)| ❌ | Very fast in practice |
| Heap Sort       | Comparison      | O(n log n)| O(n log n) | O(n log n)| O(1) | ❌     | Priority queues |
| Shell Sort      | Comparison      | O(n log n)| O(n²)      | O(n^(3/2))| O(1) | ❌     | Gap sequence |
| Comb Sort       | Comparison      | O(n log n)| O(n²)      | O(n²/2^p)| O(1) | ❌     | Bubble improvement |
| Cycle Sort      | Comparison      | O(n²)     | O(n²)      | O(n²)    | O(1)  | ❌     | Min writes |
| Counting Sort   | Non-Comparison  | O(n+k)    | O(n+k)     | O(n+k)   | O(n+k)| ✅     | Only integers |
| Radix Sort      | Non-Comparison  | O(nk)     | O(nk)      | O(nk)    | O(n+k)| ✅     | Digits-based |
| Bucket Sort     | Non-Comparison  | O(n+k)    | O(n²)      | O(n+k)   | O(n+k)| ✅     | Uniform data |
| Pigeonhole Sort | Non-Comparison  | O(n+range)| O(n+range) | O(n+range)| O(range)| ✅  | Narrow range only |
| Tim Sort        | Hybrid          | O(n)      | O(n log n) | O(n log n)| O(n) | ✅     | Python default |
| Intro Sort      | Hybrid          | O(n log n)| O(n log n) | O(n log n)| O(log n)| ❌ | C++ STL sort |

---

## 🗂️ File Structure  
```

Sorting/
├── bubble\_sort.py
├── selection\_sort.py
├── insertion\_sort.py
├── merge\_sort.py
├── quick\_sort.py
├── heap\_sort.py
├── shell\_sort.py
├── comb\_sort.py
├── cycle\_sort.py
├── counting\_sort.py
├── radix\_sort.py
├── bucket\_sort.py
├── pigeonhole\_sort.py
├── tim\_sort.py
├── intro\_sort.py
└── README.md

```
```

---

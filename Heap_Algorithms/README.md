# 📂 `Heap_Algorithms/README.md`

## 📑 Table of Contents

1. [Min Heap & Max Heap Operations](#1-min-heap--max-heap-operations)
2. [Heapify](#2-heapify)
3. [Heap Sort](#3-heap-sort)
4. [Kth Largest / Smallest Element](#4-kth-largest--smallest-element)
5. [Median of Data Stream](#5-median-of-data-stream)
6. [Top-K Frequent Elements](#6-top-k-frequent-elements)

---

## 🔹 1. Min Heap & Max Heap Operations

**Explanation:**

* A **heap** is a complete binary tree satisfying the **heap property**:

  * **Min Heap** → parent ≤ children.
  * **Max Heap** → parent ≥ children.
* Implemented using arrays for efficiency.

**Operations:**

* Insert → O(log n)
* Extract Min/Max → O(log n)
* Peek → O(1)

**Pseudocode (Insert in Min Heap):**

```
procedure insert(heap, val):
    heap.append(val)
    i = size-1
    while i > 0 and heap[parent(i)] > heap[i]:
        swap(heap[parent(i)], heap[i])
        i = parent(i)
```

---

## 🔹 2. Heapify

**Explanation:**
Convert an array into a heap in O(n).

**Steps:**

* Start from last non-leaf node → apply `sift_down`.
* Recursively maintain heap property.

**Pseudocode:**

```
procedure heapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        swap(arr[i], arr[smallest])
        heapify(arr, n, smallest)
```

---

## 🔹 3. Heap Sort

**Explanation:**
Sorting algorithm using heaps.

* Build a **max heap**.
* Extract max repeatedly and place at end.

**Pseudocode:**

```
procedure heap_sort(arr):
    build_max_heap(arr)
    for i from n-1 downto 1:
        swap(arr[0], arr[i])
        heapify(arr, i, 0)
```

**Complexity:** O(n log n).
**In-place:** Yes.
**Stable:** No.

---

## 🔹 4. Kth Largest / Smallest Element

**Approach:**

* **Kth Largest:** Min Heap of size `k`.
* **Kth Smallest:** Max Heap of size `k`.

**Pseudocode (Kth Largest):**

```
procedure kth_largest(arr, k):
    min_heap = []
    for num in arr:
        push(min_heap, num)
        if size(min_heap) > k:
            pop(min_heap)
    return min_heap[0]
```

**Complexity:** O(n log k).

---

## 🔹 5. Median of Data Stream

**Explanation:**
Maintain median while streaming numbers.

* Use **two heaps**:

  * Max Heap (lower half).
  * Min Heap (upper half).
* Balance heaps so size difference ≤ 1.

**Pseudocode:**

```
procedure add_num(num):
    if num <= max_heap.top():
        push(max_heap, num)
    else:
        push(min_heap, num)
    balance_heaps()

procedure find_median():
    if size(max_heap) == size(min_heap):
        return (max_heap.top() + min_heap.top()) / 2
    else:
        return max_heap.top() if larger else min_heap.top()
```

**Complexity:** O(log n) per insertion.

---

## 🔹 6. Top-K Frequent Elements

**Explanation:**
Find k most frequent elements using hash + heap.

**Steps:**

1. Count frequencies (hash map).
2. Push `(freq, element)` into min heap of size `k`.
3. Extract heap elements.

**Pseudocode:**

```
procedure top_k_frequent(arr, k):
    freq_map = {}
    for num in arr:
        freq_map[num] += 1
    min_heap = []
    for key, freq in freq_map:
        push(min_heap, (freq, key))
        if size(min_heap) > k:
            pop(min_heap)
    return [key for (freq, key) in min_heap]
```

**Complexity:** O(n log k).

---

## 📊 Comparison Table

| Algorithm               | Use Case                | Time                | Space |
| ----------------------- | ----------------------- | ------------------- | ----- |
| Min/Max Heap Ops        | Insert, extract min/max | O(log n)            | O(n)  |
| Heapify                 | Build heap              | O(n)                | O(1)  |
| Heap Sort               | Sorting                 | O(n log n)          | O(1)  |
| Kth Largest/Smallest    | Order statistic         | O(n log k)          | O(k)  |
| Median of Data Stream   | Online median           | O(log n) per insert | O(n)  |
| Top-K Frequent Elements | Frequency analysis      | O(n log k)          | O(n)  |

---

## 📂 File Structure

```
Heap_Algorithms/
├── min_max_heap.py
├── heapify.py
├── heap_sort.py
├── kth_largest_smallest.py
├── median_data_stream.py
├── top_k_frequent.py
└── README.md
```

---

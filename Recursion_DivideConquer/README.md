# 📂 `Recursion_DivideConquer/README.md`

## 📑 Table of Contents

1. [Tower of Hanoi](#1-tower-of-hanoi)
2. [Fibonacci (Recursive + Optimized)](#2-fibonacci-recursive--optimized)
3. [Maximum / Minimum using Divide & Conquer](#3-maximum--minimum-using-divide--conquer)
4. [Merge Sort / Quick Sort (Recursive Forms)](#4-merge-sort--quick-sort-recursive-forms)

---

## 🔹 1. Tower of Hanoi

**Explanation:**
A mathematical puzzle with 3 rods and *n* disks. Goal: move all disks from source to destination rod, following rules:

1. Only one disk can be moved at a time.
2. No disk may be placed on a smaller disk.

**Recursive Strategy:**

* Move `n-1` disks from source → auxiliary.
* Move 1 disk from source → destination.
* Move `n-1` disks from auxiliary → destination.

**Pseudocode:**

```
procedure hanoi(n, source, destination, auxiliary):
    if n == 1:
        print "Move disk 1 from source to destination"
        return
    hanoi(n-1, source, auxiliary, destination)
    print "Move disk n from source to destination"
    hanoi(n-1, auxiliary, destination, source)
```

**Complexity:** O(2^n).

---

## 🔹 2. Fibonacci (Recursive + Optimized)

**Naive Recursion:**

```
procedure fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

* Time: O(2^n)
* Space: O(n) (recursion stack).

**Optimized (Memoization):**

```
memo = {}
procedure fib(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

* Time: O(n)
* Space: O(n).

**Optimized (Bottom-Up DP):**

```
procedure fib(n):
    dp[0] = 0
    dp[1] = 1
    for i in 2..n:
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

* Time: O(n)
* Space: O(n) (or O(1) with 2 vars).

---

## 🔹 3. Maximum / Minimum using Divide & Conquer

**Explanation:**
Split array into halves recursively and compute max/min from each half.

**Pseudocode:**

```
procedure find_max(arr, l, r):
    if l == r: return arr[l]
    mid = (l + r) / 2
    left_max = find_max(arr, l, mid)
    right_max = find_max(arr, mid+1, r)
    return max(left_max, right_max)
```

**Complexity:** O(n).

---

## 🔹 4. Merge Sort / Quick Sort (Recursive Forms)

### **Merge Sort**

* Divide array into halves until size = 1.
* Merge two sorted halves.

**Pseudocode:**

```
procedure merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) / 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

**Complexity:** O(n log n).

---

### **Quick Sort**

* Choose a pivot.
* Partition array into ≤ pivot and > pivot.
* Recursively sort subarrays.

**Pseudocode:**

```
procedure quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
```

**Complexity:**

* Best/Average: O(n log n)
* Worst: O(n²) (if poor pivot).

---

## 📊 Comparison Table

| Algorithm           | Use Case                     | Time       | Space       |
| ------------------- | ---------------------------- | ---------- | ----------- |
| Tower of Hanoi      | Classic recursion puzzle     | O(2^n)     | O(n)        |
| Fibonacci (Naive)   | Compute nth Fibonacci        | O(2^n)     | O(n)        |
| Fibonacci (Memo/DP) | Optimized Fibonacci          | O(n)       | O(n) / O(1) |
| Max/Min (D\&C)      | Find max/min element         | O(n)       | O(log n)    |
| Merge Sort          | Stable divide & conquer sort | O(n log n) | O(n)        |
| Quick Sort          | Fast average-case sort       | O(n log n) | O(log n)    |

---

## 📂 File Structure

```
Recursion_DivideConquer/
├── tower_of_hanoi.py
├── fibonacci.py
├── max_min_divide_conquer.py
├── merge_sort_recursive.py
├── quick_sort_recursive.py
└── README.md
```

---

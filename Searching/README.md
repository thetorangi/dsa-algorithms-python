# 🔍 Searching Algorithms

This folder contains implementations of **fundamental searching algorithms** in Python.  
Searching is the process of finding the location of a target element within a collection of data.  

---

## 📑 Table of Contents
1. [Linear Search](#1-linear-search)
2. [Binary Search](#2-binary-search)
3. [Ternary Search](#3-ternary-search)
4. [Jump Search](#4-jump-search)
5. [Exponential Search](#5-exponential-search)
6. [Interpolation Search](#6-interpolation-search)
7. [Comparison Table](#-comparison-table)
8. [File Structure](#-file-structure)

---

## 📘 Algorithms Covered

---

### 1. Linear Search
**Explanation**: Searches each element one by one and compares it with the target.  

**Steps**:
1. Start from the first element.  
2. Compare with the target.  
3. If equal → return index.  
4. Else move to next element.  
5. If end is reached → element not present.  

**Pseudocode**:
```

procedure linearSearch(arr, target):
for i ← 0 to length(arr)-1:
if arr\[i] == target:
return i
return -1

```

**Complexity**:
- Time: O(n)  
- Space: O(1) (iterative), O(n) (recursive)

---

### 2. Binary Search
**Explanation**: Directly compares the target with the middle element,  
then shifts the search boundary to left or right half accordingly.  

**Steps**:
1. Set `low = 0`, `high = n-1`.  
2. While `low <= high`:  
   - `mid = (low + high) // 2`  
   - If `arr[mid] == target` → found  
   - If `arr[mid] > target` → search left half  
   - Else → search right half  

**Pseudocode**:
```

procedure binarySearch(arr, target):
low ← 0, high ← length(arr) - 1
while low ≤ high:
mid ← (low + high) // 2
if arr\[mid] == target:
return mid
else if arr\[mid] > target:
high ← mid - 1
else:
low ← mid + 1
return -1

```

**Complexity**:
- Time: O(log n)  
- Space: O(1) (iterative), O(log n) (recursive)  

---

### 3. Ternary Search
**Explanation**: Instead of dividing into two halves like binary search,  
it divides the range into three parts and compares with two midpoints.  

**Pseudocode**:
```

procedure ternarySearch(arr, low, high, target):
if low > high:
return -1

```
mid1 ← low + (high - low) // 3

mid2 ← high - (high - low) // 3


if arr[mid1] == target:

    return mid1
    
if arr[mid2] == target:

    return mid2
    

if target < arr[mid1]:

    return ternarySearch(arr, low, mid1-1, target)
    
else if target > arr[mid2]:

    return ternarySearch(arr, mid2+1, high, target)
    
else:

    return ternarySearch(arr, mid1+1, mid2-1, target)
    
```

```

**Complexity**:
- Time: O(log₃ n)  
- Space: O(log n) (recursive stack)  

---

### 4. Jump Search
**Explanation**: Jumps ahead in fixed block sizes (√n)  
and then performs a linear search within the identified block.  

**Pseudocode**:
```

procedure jumpSearch(arr, target):
n ← length(arr)
step ← √n
prev ← 0

```
while arr[min(step, n)-1] < target:
    prev ← step
    step ← step + √n
    if prev ≥ n:
        return -1

for i ← prev to min(step, n)-1:
    if arr[i] == target:
        return i
return -1
```

```

**Complexity**:
- Time: O(√n)  
- Space: O(1)  

---

### 5. Exponential Search
**Explanation**: Expands the range exponentially (1, 2, 4, 8, …)  
until the target range is found, then applies binary search.  

**Pseudocode**:
```

procedure exponentialSearch(arr, target):
if arr\[0] == target:
return 0

```
i ← 1
while i < length(arr) and arr[i] ≤ target:
    i ← i * 2

return binarySearch(arr, i/2, min(i, length(arr)-1), target)
```

```

**Complexity**:
- Time: O(log i), where i = index of target  
- Space: O(1)  

---

### 6. Interpolation Search
**Explanation**: Improves binary search by predicting the position  
based on the value of the target (works best on uniformly distributed data).  

**Pseudocode**:
```

procedure interpolationSearch(arr, target):
low ← 0, high ← length(arr) - 1

```
while low ≤ high and target ≥ arr[low] and target ≤ arr[high]:
    pos ← low + ((target - arr[low]) * (high - low)) 
                 // (arr[high] - arr[low])

    if arr[pos] == target:
        return pos
    else if arr[pos] < target:
        low ← pos + 1
    else:
        high ← pos - 1
return -1
```

```

**Complexity**:
- Best: O(log log n) (uniform data)  
- Worst: O(n) (skewed data)  
- Space: O(1)  

---

## 📊 Comparison Table

| Algorithm            | Best Case | Worst Case | Space | Data Requirement                | Notes |
|----------------------|-----------|------------|-------|---------------------------------|-------|
| Linear Search        | O(1)      | O(n)       | O(1)  | Works on any data               | Simple, but inefficient on large arrays |
| Binary Search        | O(1)      | O(log n)   | O(1)  | Requires sorted data            | Most commonly used |
| Ternary Search       | O(1)      | O(log₃ n)  | O(log n) | Requires sorted data          | Rare in practice |
| Jump Search          | O(√n)     | O(√n)      | O(1)  | Requires sorted data            | Trade-off between linear & binary |
| Exponential Search   | O(1)      | O(log i)   | O(1)  | Infinite or unbounded arrays    | Best when size is unknown |
| Interpolation Search | O(log log n) | O(n)    | O(1)  | Sorted & uniformly distributed  | Very fast for uniform data |

---

## 🗂️ File Structure
```

Searching/
├── linear\_search.py
├── binary\_search.py
├── ternary\_search.py
├── jump\_search.py
├── exponential\_search.py
├── interpolation\_search.py
└── README.md

```

---


## 📌 Key Takeaways
- **Linear Search** → works everywhere, but slow.  
- **Binary Search** → go-to for sorted data.  
- **Ternary Search** → mostly theoretical, niche cases.  
- **Jump Search** → compromise between linear & binary.  
- **Exponential Search** → useful for infinite/unbounded arrays.  
- **Interpolation Search** → best for uniformly distributed sorted data.  
---

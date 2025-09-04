# 🔄 Sorting Algorithms

This folder contains implementations of **fundamental and advanced sorting algorithms** in Python.  
Sorting is the process of arranging elements in a particular order (ascending/descending).  

---

## 📑 Table of Contents
1. [Bubble Sort](#1-bubble-sort)  
2. [Selection Sort](#2-selection-sort)  
3. [Insertion Sort](#3-insertion-sort)  
4. [Merge Sort](#4-merge-sort)  
5. [Quick Sort](#5-quick-sort)  
6. [Heap Sort](#6-heap-sort)  
7. [Counting Sort](#7-counting-sort)  
8. [Radix Sort](#8-radix-sort)  
9. [Bucket Sort](#9-bucket-sort)  
10. [Comparison Table](#-comparison-table)  
11. [File Structure](#-file-structure)  

---

## 📘 Algorithms Covered

---

### 1. Bubble Sort
**Explanation**: Repeatedly compares adjacent elements and swaps them if out of order. The largest element “bubbles up” to the end in each pass.  

**Pseudocode**:
```

procedure bubbleSort(arr):
n ← length(arr)
for i ← 0 to n-1:
swapped ← false
for j ← 0 to n-i-2:
if arr\[j] > arr\[j+1]:
swap(arr\[j], arr\[j+1])
swapped ← true
if swapped == false:
break

```

**Complexity**:  
- Best: O(n) (already sorted)  
- Worst: O(n²)  
- Space: O(1)  
- Stable: ✅  

---

### 2. Selection Sort
**Explanation**: Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.  

**Pseudocode**:
```

procedure selectionSort(arr):
n ← length(arr)
for i ← 0 to n-1:
minIndex ← i
for j ← i+1 to n-1:
if arr\[j] < arr\[minIndex]:
minIndex ← j
swap(arr\[i], arr\[minIndex])

```

**Complexity**:  
- Best: O(n²)  
- Worst: O(n²)  
- Space: O(1)  
- Stable: ❌  

---

### 3. Insertion Sort
**Explanation**: Builds the final sorted array one item at a time by shifting larger elements to the right.  

**Pseudocode**:
```

procedure insertionSort(arr):
n ← length(arr)
for i ← 1 to n-1:
key ← arr\[i]
j ← i-1
while j ≥ 0 and arr\[j] > key:
arr\[j+1] ← arr\[j]
j ← j-1
arr\[j+1] ← key

```

**Complexity**:  
- Best: O(n) (nearly sorted)  
- Worst: O(n²)  
- Space: O(1)  
- Stable: ✅  

---

### 4. Merge Sort
**Explanation**: Divide & Conquer → Recursively splits the array in half, sorts each half, and merges them.  

**Pseudocode**:
```

procedure mergeSort(arr):
if length(arr) > 1:
mid ← length(arr) / 2
L ← arr\[0...mid-1]
R ← arr\[mid...end]
mergeSort(L)
mergeSort(R)
merge(L, R, arr)

```

**Complexity**:  
- Best: O(n log n)  
- Worst: O(n log n)  
- Space: O(n)  
- Stable: ✅  

---

### 5. Quick Sort
**Explanation**: Divide & Conquer → Selects a pivot and partitions the array into elements smaller and greater than the pivot, then sorts recursively.  

**Pseudocode**:
```

procedure quickSort(arr, low, high):
if low < high:
p ← partition(arr, low, high)
quickSort(arr, low, p-1)
quickSort(arr, p+1, high)

procedure partition(arr, low, high):
pivot ← arr\[high]
i ← low - 1
for j ← low to high-1:
if arr\[j] < pivot:
i ← i+1
swap(arr\[i], arr\[j])
swap(arr\[i+1], arr\[high])
return i+1

```

**Complexity**:  
- Best: O(n log n)  
- Worst: O(n²) (bad pivot)  
- Space: O(log n)  
- Stable: ❌  

---

### 6. Heap Sort
**Explanation**: Builds a max-heap and repeatedly extracts the largest element to place at the end.  

**Pseudocode**:
```

procedure heapSort(arr):
n ← length(arr)
buildMaxHeap(arr, n)
for i ← n-1 to 1:
swap(arr\[0], arr\[i])
heapify(arr, 0, i)

```

**Complexity**:  
- Best: O(n log n)  
- Worst: O(n log n)  
- Space: O(1)  
- Stable: ❌  

---

### 7. Counting Sort
**Explanation**: Uses frequency counts of elements to place them directly in sorted order. Works only for integers in a limited range.  

**Pseudocode**:
```

procedure countingSort(arr, k):
count ← \[0...k]
output ← \[0...n-1]

```
for i ← 0 to n-1:
    count[arr[i]] += 1
for i ← 1 to k:
    count[i] += count[i-1]
for i ← n-1 downto 0:
    output[count[arr[i]]-1] ← arr[i]
    count[arr[i]] -= 1
```

```

**Complexity**:  
- Best: O(n + k)  
- Worst: O(n + k)  
- Space: O(n + k)  
- Stable: ✅  

---

### 8. Radix Sort
**Explanation**: Sorts numbers digit by digit using a stable sort (like Counting Sort) as a subroutine.  

**Pseudocode**:
```

procedure radixSort(arr, d):   // d = number of digits
for i ← 1 to d:
countingSort(arr, digit=i)

```

**Complexity**:  
- Best: O(nk)  
- Worst: O(nk)  
- Space: O(n + k)  
- Stable: ✅  

---

### 9. Bucket Sort
**Explanation**: Divides elements into buckets, sorts each bucket (using another algorithm), then concatenates.  

**Pseudocode**:
```

procedure bucketSort(arr):
n ← length(arr)
buckets ← empty lists
for each element in arr:
insert element into bucket based on range
for each bucket:
sort(bucket)   // e.g., insertion sort
concatenate all buckets

```

**Complexity**:  
- Best: O(n + k) (uniform distribution)  
- Worst: O(n²) (skewed distribution)  
- Space: O(n + k)  
- Stable: ✅ (if sub-sort is stable)  

---

## 📊 Comparison Table

| Algorithm      | Best Case | Worst Case | Avg Case | Space | Stable | Notes |
|----------------|-----------|------------|----------|-------|--------|-------|
| Bubble Sort    | O(n)      | O(n²)      | O(n²)    | O(1)  | ✅     | Simple, rarely used |
| Selection Sort | O(n²)     | O(n²)      | O(n²)    | O(1)  | ❌     | Fewest swaps |
| Insertion Sort | O(n)      | O(n²)      | O(n²)    | O(1)  | ✅     | Good for small/partially sorted arrays |
| Merge Sort     | O(n log n)| O(n log n) | O(n log n)| O(n) | ✅     | Divide & Conquer |
| Quick Sort     | O(n log n)| O(n²)      | O(n log n)| O(log n)| ❌ | Fast in practice |
| Heap Sort      | O(n log n)| O(n log n) | O(n log n)| O(1) | ❌     | Used in priority queues |
| Counting Sort  | O(n+k)    | O(n+k)     | O(n+k)   | O(n+k)| ✅     | Works for integers only |
| Radix Sort     | O(nk)     | O(nk)      | O(nk)    | O(n+k)| ✅     | Good for fixed-length numbers |
| Bucket Sort    | O(n+k)    | O(n²)      | O(n+k)   | O(n+k)| ✅     | Great for uniform distribution |

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
├── counting\_sort.py
├── radix\_sort.py
├── bucket\_sort.py
└── README.md

```

---
```

---
Do you want me to now generate the **Python `.py` code files** for each algorithm (starting with Bubble, Selection, Insertion) to match this README?

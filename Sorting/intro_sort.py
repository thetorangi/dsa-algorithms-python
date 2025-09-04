"""
Intro Sort Algorithm
--------------------
- Hybrid sorting algorithm (Quick Sort + Heap Sort + Insertion Sort).
- Starts with Quick Sort, switches to Heap Sort when recursion is too deep,
  and uses Insertion Sort for small partitions.
- Used in C++ STL sort().

Time Complexity:
    Best   : O(n log n)
    Worst  : O(n log n)
    Average: O(n log n)
Space Complexity: O(log n)
Stable: No
"""

import sys

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def intro_sort_util(arr, low, high, depth_limit):
    size = high - low + 1

    if size < 16:
        insertion_sort(arr, low, high)
    elif depth_limit == 0:
        heap_sort(arr[low:high+1], size)
    else:
        pivot = partition(arr, low, high)
        intro_sort_util(arr, low, pivot - 1, depth_limit - 1)
        intro_sort_util(arr, pivot + 1, high, depth_limit - 1)

def intro_sort(arr):
    max_depth = 2 * int(sys.getrecursionlimit().bit_length())
    intro_sort_util(arr, 0, len(arr) - 1, max_depth)
    return arr


# Example Usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original:", data)
    print("Sorted  :", intro_sort(data))

"""
Insertion Sort Algorithm
------------------------
- Comparison-based sorting
- Builds the sorted array one item at a time by shifting larger elements.

Time Complexity:
    Best   : O(n)     (nearly sorted)
    Worst  : O(n^2)
    Average: O(n^2)
Space Complexity: O(1)
Stable: Yes
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


data = [12, 11, 13, 5, 6]
print("Original:", data)
print("Sorted  :", insertion_sort(data))

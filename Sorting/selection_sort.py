"""
Selection Sort Algorithm
------------------------
- Comparison-based sorting
- Repeatedly finds the minimum element and places it at the beginning.

Time Complexity:
    Best   : O(n^2)
    Worst  : O(n^2)
    Average: O(n^2)
Space Complexity: O(1)
Stable: No
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


data = [64, 25, 12, 22, 11]
print("Original:", data)
print("Sorted  :", selection_sort(data))

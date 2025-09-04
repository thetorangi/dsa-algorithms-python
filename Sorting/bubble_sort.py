"""
Bubble Sort Algorithm
---------------------
- Comparison-based sorting
- Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
- Largest elements "bubble up" to the end of the list in each pass.

Time Complexity:
    Best   : O(n)     (already sorted)
    Worst  : O(n^2)
    Average: O(n^2)
Space Complexity: O(1)
Stable: Yes
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
print("Sorted  :", bubble_sort(data))

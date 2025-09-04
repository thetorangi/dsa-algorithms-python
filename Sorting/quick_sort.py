"""
Quick Sort Algorithm
--------------------
- Comparison-based sorting
- Divide & Conquer approach:
    1. Choose a pivot element.
    2. Partition array into two parts (smaller and larger than pivot).
    3. Recursively sort the partitions.

Time Complexity:
    Best   : O(n log n)
    Worst  : O(n^2) (bad pivot choice)
    Average: O(n log n)
Space Complexity: O(log n) due to recursion
Stable: No
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


# Example Usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original:", data)
    print("Sorted  :", quick_sort(data))

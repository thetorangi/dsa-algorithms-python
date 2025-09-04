"""
Heap Sort Algorithm
-------------------
- Comparison-based sorting
- Uses a max-heap to repeatedly extract the maximum element.

Steps:
    1. Build a max heap.
    2. Swap root with the last element.
    3. Reduce heap size and heapify.
    4. Repeat until sorted.

Time Complexity:
    Best   : O(n log n)
    Worst  : O(n log n)
    Average: O(n log n)
Space Complexity: O(1)
Stable: No
"""

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

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Example Usage
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Original:", data)
    print("Sorted  :", heap_sort(data))

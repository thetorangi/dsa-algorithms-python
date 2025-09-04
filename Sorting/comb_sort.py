"""
Comb Sort Algorithm
-------------------
- Comparison-based sorting
- Improvement over Bubble Sort.
- Uses a shrinking gap to eliminate "turtles" (small values near the end).

Time Complexity:
    Best   : O(n log n)
    Worst  : O(n^2)
    Average: O(n^2 / 2^p) (better than bubble sort)
Space Complexity: O(1)
Stable: No
"""

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
            i += 1
    return arr


# Example Usage
if __name__ == "__main__":
    data = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    print("Original:", data)
    print("Sorted  :", comb_sort(data))

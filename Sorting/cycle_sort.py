"""
Cycle Sort Algorithm
--------------------
- Comparison-based sorting
- Minimizes the number of writes (good for memory write-limited systems).
- Places each element directly into its correct position.

Time Complexity:
    Best   : O(n^2)
    Worst  : O(n^2)
    Average: O(n^2)
Space Complexity: O(1)
Stable: No
"""

def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
    return arr


# Example Usage
if __name__ == "__main__":
    data = [5, 2, 9, 5, 2, 3]
    print("Original:", data)
    print("Sorted  :", cycle_sort(data))

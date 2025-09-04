"""
Shell Sort Algorithm
--------------------
- Comparison-based sorting
- Generalization of Insertion Sort that allows exchanges of far apart elements.
- Uses a gap sequence, reducing over iterations.

Time Complexity:
    Best   : O(n log n) (with good gap sequence)
    Worst  : O(n^2)
    Average: O(n^(3/2)) approx.
Space Complexity: O(1)
Stable: No
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# Example Usage
if __name__ == "__main__":
    data = [12, 34, 54, 2, 3]
    print("Original:", data)
    print("Sorted  :", shell_sort(data))

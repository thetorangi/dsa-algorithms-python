"""
Tim Sort Algorithm
------------------
- Hybrid sorting algorithm (Merge Sort + Insertion Sort).
- Default sorting algorithm in Python (sorted(), list.sort()).
- Divides array into runs, sorts them with Insertion Sort, then merges.

Time Complexity:
    Best   : O(n)
    Worst  : O(n log n)
    Average: O(n log n)
Space Complexity: O(n)
Stable: Yes
"""

def tim_sort(arr):
    return sorted(arr)  # Python's built-in implementation (Timsort)


# Example Usage
if __name__ == "__main__":
    data = [5, 21, 7, 23, 19]
    print("Original:", data)
    print("Sorted  :", tim_sort(data))

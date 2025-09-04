"""
Bucket Sort Algorithm
---------------------
- Non-comparison-based sorting
- Distributes elements into buckets, sorts each bucket individually, then concatenates.

Time Complexity:
    Best   : O(n + k)
    Worst  : O(n^2) (if all elements fall into one bucket)
    Average: O(n + k)
Space Complexity: O(n + k)
Stable: Yes (depends on sub-sorting method)
"""

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements
    max_val, min_val = max(arr), min(arr)
    for num in arr:
        index = (num - min_val) * (bucket_count - 1) // (max_val - min_val + 1)
        buckets[index].append(num)

    # Sort buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr


# Example Usage
if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Original:", data)
    print("Sorted  :", bucket_sort(data))

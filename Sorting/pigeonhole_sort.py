"""
Pigeonhole Sort Algorithm
-------------------------
- Non-comparison-based sorting
- Works when number of elements and range are approximately the same.

Time Complexity:
    Best   : O(n + range)
    Worst  : O(n + range)
    Average: O(n + range)
Space Complexity: O(n + range)
Stable: Yes
"""

def pigeonhole_sort(arr):
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    size = max_val - min_val + 1

    # Initialize pigeonholes
    holes = [0] * size

    # Fill holes
    for num in arr:
        holes[num - min_val] += 1

    # Build sorted array
    sorted_arr = []
    for i in range(size):
        while holes[i] > 0:
            sorted_arr.append(i + min_val)
            holes[i] -= 1

    return sorted_arr


# Example Usage
if __name__ == "__main__":
    data = [8, 3, 2, 7, 4, 6, 8]
    print("Original:", data)
    print("Sorted  :", pigeonhole_sort(data))

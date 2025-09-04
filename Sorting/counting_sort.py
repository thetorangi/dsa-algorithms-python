"""
Counting Sort Algorithm
-----------------------
- Non-comparison-based sorting
- Works only for integers within a known range.
- Counts occurrences of each element, then reconstructs the sorted array.

Time Complexity:
    Best   : O(n + k)
    Worst  : O(n + k)
    Average: O(n + k)
Space Complexity: O(n + k)
Stable: Yes
(where n = number of elements, k = range of input)
"""

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store counts
    for num in arr:
        count[num - min_val] += 1

    # Prefix sums
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output (stable sorting)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


# Example Usage
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", data)
    print("Sorted  :", counting_sort(data))

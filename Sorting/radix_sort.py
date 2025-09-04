"""
Radix Sort Algorithm
--------------------
- Non-comparison-based sorting
- Sorts numbers digit by digit using a stable sorting algorithm (Counting Sort).

Time Complexity:
    Best   : O(nk)
    Worst  : O(nk)
    Average: O(nk)
Space Complexity: O(n + k)
Stable: Yes
(where n = number of elements, k = number of digits)
"""

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Prefix sums
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (stable)
    for num in reversed(arr):
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    return output

def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_exp(arr, exp)
        exp *= 10
    return arr


# Example Usage
if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original:", data)
    print("Sorted  :", radix_sort(data))

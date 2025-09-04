def ternary_search(arr, target):
    """
    Perform Ternary Search on a sorted array.

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Divide array into 3 parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if target is at mid1 or mid2
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Decide which segment to search
        if target < arr[mid1]:
            right = mid1 - 1  # Search in left segment
        elif target > arr[mid2]:
            left = mid2 + 1   # Search in right segment
        else:
            left = mid1 + 1   # Search in middle segment
            right = mid2 - 1

    return -1  # Not found


# Example usage

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 97
index = ternary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")

# 📂 `TwoPointers_SlidingWindow/README.md`

## 📑 Table of Contents

1. [Two Pointer Technique](#1-two-pointer-technique)
2. [Fixed-Size Sliding Window](#2-fixed-size-sliding-window)
3. [Variable-Size Sliding Window](#3-variable-size-sliding-window)
4. [Fast & Slow Pointers (Cycle Detection)](#4-fast--slow-pointers-cycle-detection)

---

## 🔹 1. Two Pointer Technique

**Explanation:**
The **two pointer technique** is used when the array is **sorted** or when we want to process elements from both ends.
Applications:

* Pair sum (find two numbers with given target).
* Remove duplicates from sorted array.
* Merging two sorted arrays.

**Steps (for pair sum example):**

1. Initialize `left = 0`, `right = n-1`.
2. If `arr[left] + arr[right] == target`, return pair.
3. If sum < target → move `left++`.
4. If sum > target → move `right--`.

**Pseudocode (Pair Sum):**

```
procedure two_pointer_pair_sum(arr, target):
    left = 0, right = n-1
    while left < right:
        if arr[left] + arr[right] == target:
            return (left, right)
        else if arr[left] + arr[right] < target:
            left++
        else:
            right--
    return None
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 🔹 2. Fixed-Size Sliding Window

**Explanation:**
Used when the window size `k` is **fixed** (e.g., find max sum of subarray of size `k`).
Instead of recalculating sum for each subarray, update it in O(1).

**Steps:**

1. Compute sum of first `k` elements.
2. Slide window: subtract element leaving, add new element entering.
3. Track maximum sum.

**Pseudocode:**

```
procedure max_sum_subarray(arr, k):
    window_sum = sum(arr[0..k-1])
    max_sum = window_sum
    for i from k to n-1:
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 🔹 3. Variable-Size Sliding Window

**Explanation:**
Used when the window size is **not fixed** — expands/shrinks depending on conditions.
Applications:

* Longest substring with unique characters.
* Longest subarray with sum ≤ k.

**Steps (Longest substring with unique characters):**

1. Use a hashmap/set to track elements inside window.
2. Expand `right` until condition breaks.
3. Shrink `left` until condition is satisfied again.
4. Track maximum length.

**Pseudocode:**

```
procedure longest_unique_substring(s):
    left = 0
    seen = {}
    max_len = 0
    for right in range(0, n):
        while s[right] in seen:
            remove s[left] from seen
            left++
        add s[right] to seen
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Complexity:**

* Time: O(n)
* Space: O(k) (k = character set size)

---

## 🔹 4. Fast & Slow Pointers (Cycle Detection)

**Explanation:**
Also known as **Floyd’s Cycle Detection Algorithm**.
Used in linked lists/arrays to detect **cycles**.

**Steps:**

1. Initialize `slow = head`, `fast = head`.
2. Move `slow` by 1 step, `fast` by 2 steps.
3. If `slow == fast`, a cycle exists.
4. To find cycle start: reset `slow = head` and move both by 1 step until they meet.

**Pseudocode:**

```
procedure detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 📊 Comparison Table

| Technique                    | Use Case                                  | Time Complexity | Space Complexity |
| ---------------------------- | ----------------------------------------- | --------------- | ---------------- |
| Two Pointer Technique        | Sorted arrays, pair sum, duplicates       | O(n)            | O(1)             |
| Fixed-Size Sliding Window    | Max/min subarray of fixed length          | O(n)            | O(1)             |
| Variable-Size Sliding Window | Longest substring/subarray with condition | O(n)            | O(k)             |
| Fast & Slow Pointers         | Cycle detection in linked list/array      | O(n)            | O(1)             |

---

## 📂 File Structure

```
TwoPointers_SlidingWindow/
├── two_pointer.py
├── fixed_window.py
├── variable_window.py
├── fast_slow_pointer.py
└── README.md
```

---

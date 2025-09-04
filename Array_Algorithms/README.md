# 📂 `Array_Algorithms/README.md`

## 📑 Table of Contents

1. [Kadane’s Algorithm (Maximum Subarray Sum)](#1-kadanes-algorithm-maximum-subarray-sum)
2. [Prefix Sum Technique](#2-prefix-sum-technique)
3. [Difference Array Technique](#3-difference-array-technique)
4. [Moore’s Voting Algorithm (Majority Element)](#4-moores-voting-algorithm-majority-element)
5. [Dutch National Flag Algorithm](#5-dutch-national-flag-algorithm)
6. [Maximum Product Subarray](#6-maximum-product-subarray)
7. [Trapping Rainwater](#7-trapping-rainwater)
8. [Rotate Array (Reversal Algorithm)](#8-rotate-array-reversal-algorithm)
9. [Maximum Circular Subarray Sum](#9-maximum-circular-subarray-sum)

---

## 🔹 1. Kadane’s Algorithm (Maximum Subarray Sum)

**Explanation:**
Finds the maximum sum of a contiguous subarray.
Instead of trying all subarrays (O(n²)), it keeps track of:

* `current_sum`: max subarray sum ending at current index
* `max_sum`: global maximum so far

**Steps:**

1. Initialize `current_sum = 0`, `max_sum = -∞`.
2. Traverse the array.
3. For each element: `current_sum = max(arr[i], current_sum + arr[i])`.
4. Update `max_sum = max(max_sum, current_sum)`.

**Pseudocode:**

```
procedure kadane(arr):
    max_sum ← -∞
    current_sum ← 0
    for x in arr:
        current_sum ← max(x, current_sum + x)
        max_sum ← max(max_sum, current_sum)
    return max_sum
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 🔹 2. Prefix Sum Technique

**Explanation:**
Precomputes cumulative sums so that **range sum queries** can be answered in O(1).

**Steps:**

1. Build prefix array: `prefix[i] = prefix[i-1] + arr[i]`.
2. Range sum `[l, r]` = `prefix[r] - prefix[l-1]`.

**Pseudocode:**

```
procedure build_prefix_sum(arr):
    prefix[0] = arr[0]
    for i from 1 to n-1:
        prefix[i] = prefix[i-1] + arr[i]

procedure range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]
```

**Complexity:**

* Preprocessing: O(n)
* Query: O(1)
* Space: O(n)

---

## 🔹 3. Difference Array Technique

**Explanation:**
Efficient for applying **multiple range updates**.

**Steps:**

1. Create `diff[]` of size `n+1` initialized with 0.
2. For update `(l, r, val)`:

   * `diff[l] += val`
   * `diff[r+1] -= val`
3. Reconstruct array using prefix sum.

**Pseudocode:**

```
procedure range_update(diff, l, r, val):
    diff[l] += val
    diff[r+1] -= val

procedure build_array(diff, n):
    arr[0] = diff[0]
    for i from 1 to n-1:
        arr[i] = arr[i-1] + diff[i]
    return arr
```

**Complexity:**

* Update: O(1)
* Build: O(n)
* Space: O(n)

---

## 🔹 4. Moore’s Voting Algorithm (Majority Element)

**Explanation:**
Finds the element that appears more than `n/2` times (if it exists).

**Steps:**

1. Candidate selection phase: cancel out pairs of different elements.
2. Verification phase: check if candidate really appears > n/2 times.

**Pseudocode:**

```
procedure moore_voting(arr):
    count = 0
    candidate = None
    for x in arr:
        if count == 0:
            candidate = x
        if x == candidate:
            count += 1
        else:
            count -= 1
    return candidate
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 🔹 5. Dutch National Flag Algorithm

**Explanation:**
Sort an array containing only {0, 1, 2} in one pass.

**Steps:**

* Maintain 3 pointers: `low`, `mid`, `high`.
* Traverse array and swap elements into correct regions.

**Pseudocode:**

```
procedure dutch_flag(arr):
    low = 0, mid = 0, high = n-1
    while mid <= high:
        if arr[mid] == 0:
            swap(arr[low], arr[mid])
            low++, mid++
        else if arr[mid] == 1:
            mid++
        else:
            swap(arr[mid], arr[high])
            high--
```

**Complexity:**

* Time: O(n)
* Space: O(1)

---

## 🔹 6. Maximum Product Subarray

**Explanation:**
Handles negative numbers (since `- * - = +`).
Keeps track of **max product so far** and **min product so far**.

**Steps:**

* At each index,

  * `max_prod = max(arr[i], arr[i]*max_prod, arr[i]*min_prod)`
  * `min_prod = min(arr[i], arr[i]*max_prod, arr[i]*min_prod)`

**Complexity:** O(n), O(1).

---

## 🔹 7. Trapping Rainwater

**Explanation:**
For each index, water trapped = `min(max_left, max_right) - height[i]`.
Use two pointers and running maxima for O(n) time, O(1) space.

**Pseudocode:**

```
procedure trap_water(height):
    left, right = 0, n-1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left++
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right--
    return water
```

---

## 🔹 8. Rotate Array (Reversal Algorithm)

**Explanation:**
Rotate an array right by `k` positions in-place using reversals.

**Steps:**

1. Reverse entire array.
2. Reverse first `k` elements.
3. Reverse remaining `n-k` elements.

**Pseudocode:**

```
procedure reverse(arr, l, r):
    while l < r:
        swap(arr[l], arr[r])
        l++, r--

procedure rotate(arr, k):
    n = length(arr)
    k = k mod n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
```

---

## 🔹 9. Maximum Circular Subarray Sum

**Explanation:**
The maximum sum subarray is either:

1. **Normal Kadane’s result**, OR
2. **Total sum – minimum subarray sum** (wraparound case).
   Handle all-negative case separately.

**Pseudocode:**

```
procedure max_circular_subarray(arr):
    max_kadane = kadane(arr)
    total_sum = sum(arr)
    min_kadane = kadane([-x for x in arr]) * -1
    if total_sum == min_kadane:
        return max_kadane
    return max(max_kadane, total_sum - min_kadane)
```

---

## 📊 Comparison Table

| Algorithm                         | Use Case             | Time   | Space | Notes                     |
| --------------------------------- | -------------------- | ------ | ----- | ------------------------- |
| Kadane’s Algorithm                | Max subarray sum     | O(n)   | O(1)  | Handles negatives         |
| Prefix Sum                        | Range sum queries    | O(n+q) | O(n)  | Fast queries              |
| Difference Array                  | Range updates        | O(n+q) | O(n)  | Useful in offline updates |
| Moore’s Voting Algorithm          | Majority element     | O(n)   | O(1)  | Needs verification        |
| Dutch National Flag Algorithm     | Sort 0s,1s,2s        | O(n)   | O(1)  | 1-pass                    |
| Maximum Product Subarray          | Max product subarray | O(n)   | O(1)  | Handles negatives         |
| Trapping Rainwater                | Water trapped        | O(n)   | O(1)  | Two-pointer trick         |
| Rotate Array (Reversal Algorithm) | Rotate array by k    | O(n)   | O(1)  | In-place                  |
| Maximum Circular Subarray Sum     | Circular max sum     | O(n)   | O(1)  | Uses Kadane               |

---

## 📂 File Structure

```
Array_Algorithms/
├── kadane.py
├── prefix_sum.py
├── difference_array.py
├── moore_voting.py
├── dutch_national_flag.py
├── max_product_subarray.py
├── trapping_rainwater.py
├── rotate_array.py
├── max_circular_subarray.py
└── README.md
```

---

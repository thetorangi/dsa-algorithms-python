# 📂 `DynamicProgramming/README.md`

## 📑 Table of Contents

1. [Fibonacci (Memoization + Tabulation)](#1-fibonacci-memoization--tabulation)
2. [Climbing Stairs](#2-climbing-stairs)
3. [Longest Common Subsequence (LCS)](#3-longest-common-subsequence-lcs)
4. [Longest Increasing Subsequence (LIS)](#4-longest-increasing-subsequence-lis)
5. [0/1 Knapsack](#5-01-knapsack)
6. [Subset Sum / Partition Equal Subset](#6-subset-sum--partition-equal-subset)
7. [Coin Change (Min Coins & Count Ways)](#7-coin-change-min-coins--count-ways)
8. [Matrix Chain Multiplication](#8-matrix-chain-multiplication)
9. [Edit Distance (Levenshtein)](#9-edit-distance-levenshtein)

---

## 🔹 1. Fibonacci (Memoization + Tabulation)

**Memoization (Top-Down):** Store computed results.

```
procedure fib(n, memo):
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

**Tabulation (Bottom-Up):** Iterative DP.

```
procedure fib(n):
    dp[0]=0, dp[1]=1
    for i=2..n:
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
```

* Time: O(n)
* Space: O(n) or O(1) (optimized).

---

## 🔹 2. Climbing Stairs

**Problem:** Ways to climb `n` stairs taking 1 or 2 steps.

```
procedure climb(n):
    dp[0]=1, dp[1]=1
    for i=2..n:
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
```

* Time: O(n)
* Space: O(1).

---

## 🔹 3. Longest Common Subsequence (LCS)

**Problem:** Find length of longest subsequence common to both strings.

```
procedure lcs(a, b):
    dp = matrix(len(a)+1, len(b)+1)
    for i=1..len(a):
        for j=1..len(b):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

* Time: O(m·n)
* Space: O(m·n).

---

## 🔹 4. Longest Increasing Subsequence (LIS)

**Problem:** Find LIS length.

```
procedure lis(arr):
    dp = [1]*n
    for i=1..n:
        for j=0..i-1:
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
```

* Time: O(n²) (can be O(n log n) with binary search).
* Space: O(n).

---

## 🔹 5. 0/1 Knapsack

**Problem:** Max value with weight constraint.

```
procedure knapsack(W, wt[], val[], n):
    dp[n+1][W+1]
    for i=0..n:
        for w=0..W:
            if i==0 or w==0: dp[i][w]=0
            else if wt[i-1] <= w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]
```

* Time: O(n·W)
* Space: O(n·W).

---

## 🔹 6. Subset Sum / Partition Equal Subset

**Problem:** Check if subset sums to target.

```
procedure subset_sum(arr, target):
    dp[n+1][target+1]
    dp[0][0] = True
    for i=1..n:
        for j=0..target:
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    return dp[n][target]
```

* Time: O(n·target).
* Space: O(n·target).

---

## 🔹 7. Coin Change (Min Coins & Count Ways)

**Min Coins Problem:**

```
procedure coin_change_min(coins, amount):
    dp[0]=0, rest=inf
    for i=1..amount:
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amount]
```

**Count Ways Problem:**

```
procedure coin_change_count(coins, amount):
    dp[0]=1
    for coin in coins:
        for i=coin..amount:
            dp[i] += dp[i-coin]
    return dp[amount]
```

* Time: O(n·amount).
* Space: O(amount).

---

## 🔹 8. Matrix Chain Multiplication (MCM)

**Problem:** Parenthesize matrices for min multiplication cost.

```
procedure mcm(dims):
    n=len(dims)-1
    dp[n][n]
    for l=2..n:
        for i=0..n-l:
            j=i+l-1
            dp[i][j]=inf
            for k=i..j-1:
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                dp[i][j]=min(dp[i][j], cost)
    return dp[0][n-1]
```

* Time: O(n³)
* Space: O(n²).

---

## 🔹 9. Edit Distance (Levenshtein)

**Problem:** Min operations (insert, delete, replace) to convert str1 → str2.

```
procedure edit_distance(s1, s2):
    dp[len1+1][len2+1]
    for i=0..len1: dp[i][0]=i
    for j=0..len2: dp[0][j]=j
    for i=1..len1:
        for j=1..len2:
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len1][len2]
```

* Time: O(m·n)
* Space: O(m·n).

---

## 📊 Comparison Table

| Algorithm                   | Time Complexity    | Space Complexity | Notes                |
| --------------------------- | ------------------ | ---------------- | -------------------- |
| Fibonacci (DP)              | O(n)               | O(1)             | Base DP example      |
| Climbing Stairs             | O(n)               | O(1)             | Similar to Fibonacci |
| LCS                         | O(m·n)             | O(m·n)           | String DP classic    |
| LIS (DP)                    | O(n²) / O(n log n) | O(n)             | Can optimize         |
| 0/1 Knapsack                | O(n·W)             | O(n·W)           | Core DP problem      |
| Subset Sum                  | O(n·target)        | O(n·target)      | Boolean DP           |
| Coin Change (min/count)     | O(n·amount)        | O(amount)        | Two variants         |
| Matrix Chain Multiplication | O(n³)              | O(n²)            | Interval DP          |
| Edit Distance               | O(m·n)             | O(m·n)           | String DP            |

---

## 📂 File Structure

```
DynamicProgramming/
├── fibonacci.py
├── climbing_stairs.py
├── lcs.py
├── lis.py
├── knapsack.py
├── subset_sum.py
├── coin_change.py
├── matrix_chain.py
├── edit_distance.py
└── README.md
```

---

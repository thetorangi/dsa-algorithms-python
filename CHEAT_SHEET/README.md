# Complete DSA Patterns Reference Guide

## Core Problem-Solving Patterns
# DSA Patterns with LeetCode Links (1-31)

| No. | Pattern | Description | Key Idea | Example Problems & LeetCode Links |
|-----|---------|-------------|----------|-----------------------------------|
| 1 | **Sliding Window** | Used for problems involving subarrays or substrings. | Use a sliding window to optimize time complexity from O(n²) to O(n). | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 2 | **Two Pointers** | Used for problems involving sorted arrays, linked lists, or string manipulation. | Use two pointers moving towards/away from each other. | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |
| 3 | **Fast and Slow Pointers** | Used for cyclic problems like finding loops in linked lists. | Use two pointers moving at different speeds. | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) |
| 4 | **Merge Intervals** | Used for problems involving overlapping intervals. | Sort intervals and merge based on conditions. | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/), [57. Insert Interval](https://leetcode.com/problems/insert-interval/) |
| 5 | **Cyclic Sort** | Used for problems involving numbers in a given range (1 to n). | Place each number at its correct index. | [268. Missing Number](https://leetcode.com/problems/missing-number/), [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) |
| 6 | **Subsets** | Used for problems requiring all combinations/sub sets of elements. | Use BFS, recursion, or bitmasking. | [78. Subsets](https://leetcode.com/problems/subsets/), [46. Permutations](https://leetcode.com/problems/permutations/) |
| 7 | **Binary Search** | Used for searching in sorted arrays or answer-based problems. | Divide and conquer; halve the search space. | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), [704. Binary Search](https://leetcode.com/problems/binary-search/) |
| 8 | **Backtracking** | Used for constraint-based problems like permutations and combinations. | Try all possibilities and backtrack upon failure. | [51. N-Queens](https://leetcode.com/problems/n-queens/), [79. Word Search](https://leetcode.com/problems/word-search/) |
| 9 | **Breadth-First Search (BFS)** | Used for shortest path or level-order traversal problems. | Explore all neighbors at the current level before moving to the next level. | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [127. Word Ladder](https://leetcode.com/problems/word-ladder/) |
| 10 | **Depth-First Search (DFS)** | Used for pathfinding, tree/graph traversal and connected components. | Recursively or iteratively explore each path fully. | [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/), [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 11 | **Topological Sort** | Used for problems with dependencies in a Directed Acyclic Graph (DAG). | Use BFS or DFS to order tasks based on prerequisites. | [207. Course Schedule](https://leetcode.com/problems/course-schedule/), [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| 12 | **Union-Find (Disjoint Set)** | Used for connectivity in graphs. | Use union and find operations to manage connected components. | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/), [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) |
| 13 | **Greedy** | Used for optimization problems (minimizing/maximizing something). | Make the locally optimal choice at each step. | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/), [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) |
| 14 | **Dynamic Programming (DP)** | Used for optimization and decision-based problems. | Break the problem into overlapping subproblems. | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| 15 | **Bit Manipulation** | Used for binary-related problems like subsets and XOR queries. | Use bitwise operators to solve efficiently. | [136. Single Number](https://leetcode.com/problems/single-number/), [231. Power of Two](https://leetcode.com/problems/power-of-two/) |
| 16 | **Matrix Traversal** | Used for problems involving grid traversal. | Use BFS, DFS, or dynamic programming. | [62. Unique Paths](https://leetcode.com/problems/unique-paths/), [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) |
| 17 | **Heap / Priority Queue** | Used for problems requiring frequent max/min operations. | Use heaps for efficient insertion and extraction. | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/), [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 18 | **Divide and Conquer** | Used for problems involving partitioning. | Divide the problem into smaller subproblems. | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/), [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |
| 19 | **Prefix Sum** | Used for problems involving range sums. | Precompute cumulative sums to optimize queries. | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/), [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) |
| 20 | **Sliding Window** | Used for problems involving subarrays or substrings. | Use a sliding window to optimize time complexity from O(n²) to O(n). | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 21 | **Kadane's Algorithm** | Used for maximum subarray problems. | Maintain a running sum and update the max sum. | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) |
| 22 | **Trie (Prefix Tree)** | Used for word-related problems. | Use a tree structure for fast prefix lookups. | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/), [212. Word Search II](https://leetcode.com/problems/word-search-ii/) |
| 23 | **Segment Trees** | Used for range query problems. | Build a tree structure for efficient range queries. | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/), [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 24 | **Graph Traversal** | Used for graph-related problems like shortest paths or connected components. | Use DFS, BFS, or Dijkstra's algorithm. | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/), [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) |
| 25 | **Flood Fill** | Used for grid-based coloring or connected regions. | Use DFS or BFS to visit all connected components. | [733. Flood Fill](https://leetcode.com/problems/flood-fill/), [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) |
| 26 | **Monotonic Stack** | Used for problems involving nearest larger/smaller elements. | Use a stack to maintain a monotonic sequence. | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/), [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 27 | **String Matching (KMP, Rabin-Karp)** | Used for finding substrings in a string. | Use efficient string matching algorithms. | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/), [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) |
| 28 | **Binary Indexed Tree (Fenwick Tree)** | Used for dynamic range sum/updates. | Use a tree structure to efficiently compute prefix sums. | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/), [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 29 | **Reservoir Sampling** | Used for random sampling. | Keep track of k items randomly selected from a stream. | [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/), [398. Random Pick Index](https://leetcode.com/problems/random-pick-index/) |
| 30 | **LRU Cache** | Used for caching problems. | Use a hashmap and doubly linked list. | [146. LRU Cache](https://leetcode.com/problems/lru-cache/), [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) |
| 31 | **Fibonacci Sequence** | Used for DP problems. | Compute Fibonacci numbers iteratively or using matrix exponentiation. | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), [198. House Robber](https://leetcode.com/problems/house-robber/) |

## Additional Important Patterns

| No. | Pattern | Description | Key Idea | Example Problems & LeetCode Links |
|-----|---------|-------------|----------|-----------------------------------|
| 32 | **Morris Traversal** | Used for tree traversal without extra space. | Use threading to traverse without recursion/stack. | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/), [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |
| 33 | **Boyer-Moore Majority Vote** | Used for finding majority elements. | Use voting algorithm to find majority in O(n) time. | [169. Majority Element](https://leetcode.com/problems/majority-element/), [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) |
| 34 | **Rolling Hash** | Used for string/array comparison problems. | Use polynomial rolling hash for efficient comparisons. | [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/), [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) |
| 35 | **Manacher's Algorithm** | Used for palindrome problems. | Find all palindromes in linear time. | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/), [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |
| 36 | **Catalan Numbers** | Used for counting problems with nested structures. | Count valid combinations of nested elements. | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/), [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) |
| 37 | **Sqrt Decomposition** | Used for range queries with updates. | Divide array into √n blocks for balanced operations. | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/), [Range Minimum Query](https://www.spoj.com/problems/RMQSQ/) |
| 38 | **Heavy-Light Decomposition** | Used for tree path queries. | Decompose tree into heavy and light edges. | [Path Queries on Trees](https://cses.fi/problemset/task/1138), [Tree Path Queries](https://codeforces.com/problemset/problem/208/E) |
| 39 | **Convex Hull** | Used for computational geometry problems. | Find the convex hull of a set of points. | [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/), [Farthest Pair](https://www.spoj.com/problems/CLOSEST/) |
| 40 | **Game Theory (Minimax)** | Used for game-playing problems. | Use minimax with alpha-beta pruning. | [464. Can I Win](https://leetcode.com/problems/can-i-win/), [877. Stone Game](https://leetcode.com/problems/stone-game/) |
| 41 | **Meet in the Middle** | Used for optimization when brute force is O(2^n). | Split problem space and combine results. | [18. 4Sum](https://leetcode.com/problems/4sum/), [1755. Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) |
| 42 | **Coordinate Compression** | Used when dealing with large coordinate ranges. | Map large coordinates to smaller range. | [391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/), [850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) |
| 43 | **Persistent Data Structures** | Used when you need to maintain multiple versions. | Keep history of data structure modifications. | [Version Control](https://codeforces.com/contest/1015/problem/F), [Range Queries](https://www.spoj.com/problems/COT/) |
| 44 | **Network Flow (Max Flow)** | Used for flow optimization problems. | Find maximum flow through a network. | [Maximum Bipartite Matching](https://www.spoj.com/problems/MATCHING/), [Max Flow](https://cses.fi/problemset/task/1694) |
| 45 | **Shortest Path Algorithms** | Used for graph path problems. | Dijkstra's, Bellman-Ford, Floyd-Warshall. | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/), [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |
| 46 | **Strongly Connected Components** | Used for directed graph connectivity. | Kosaraju's or Tarjan's algorithm. | [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/), [Strongly Connected Components](https://www.spoj.com/problems/BOTTOM/) |
| 47 | **Articulation Points/Bridges** | Used for finding critical nodes/edges in graphs. | Use DFS with low-link values. | [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/), [Articulation Points](https://www.spoj.com/problems/SUBMERGE/) |
| 48 | **Line Sweep** | Used for computational geometry problems. | Process events in sorted order. | [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/), [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) |
| 49 | **Z-Algorithm** | Used for string matching problems. | Find all occurrences of pattern in text. | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/), [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) |
| 50 | **Suffix Array/Tree** | Used for string processing problems. | Efficient substring operations. | [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/), [Suffix Array](https://www.spoj.com/problems/SARRAY/) |

## Time and Space Complexity Quick Reference

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Binary Search | O(log n) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) |
| Heap Operations | O(log n) | O(1) for operations |
| Hash Table Operations | O(1) avg, O(n) worst | O(n) |
| DFS/BFS | O(V + E) | O(V) |
| Dijkstra's Algorithm | O((V + E) log V) | O(V) |
| Dynamic Programming | Varies (usually O(n²) or O(n³)) | O(n) to O(n²) |
| Union-Find | O(α(n)) amortized | O(n) |
| Trie Operations | O(m) where m is key length | O(ALPHABET_SIZE × N × M) |

## Pattern Selection Guide

**For Array/String Problems:**
- Use Sliding Window for subarray/substring problems
- Use Two Pointers for sorted arrays or palindromes
- Use Prefix Sum for range sum queries
- Use Binary Search for sorted arrays or answer-based problems

**For Tree/Graph Problems:**
- Use DFS for path problems and tree traversal
- Use BFS for shortest path and level-order traversal
- Use Union-Find for connectivity problems
- Use Topological Sort for dependency problems

**For Optimization Problems:**
- Use Dynamic Programming for overlapping subproblems
- Use Greedy for locally optimal choices
- Use Backtracking for constraint satisfaction

**For Data Structure Design:**
- Use Heap for priority-based operations
- Use Trie for word/prefix problems
- Use Segment Tree for range queries with updates
- Use Hash Map for fast lookups and counting


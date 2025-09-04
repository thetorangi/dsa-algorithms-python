# 📂 `Queue_Deque_Algorithms/README.md`

## 📑 Table of Contents

1. [Circular Queue Implementation](#1-circular-queue-implementation)
2. [Deque Applications (Sliding Window Maximum)](#2-deque-applications-sliding-window-maximum)
3. [LRU Cache (Queue + Hashing)](#3-lru-cache-queue--hashing)
4. [Multi-source BFS (Rotten Oranges type)](#4-multi-source-bfs-rotten-oranges-type)

---

## 🔹 1. Circular Queue Implementation

**Explanation:**
A **circular queue** is a fixed-size queue where the last position connects back to the first (circular array).
Efficiently handles enqueue/dequeue without shifting elements.

**Steps:**

* Maintain `front`, `rear`, `size`.
* Enqueue: insert at `rear = (rear + 1) % capacity`.
* Dequeue: remove from `front = (front + 1) % capacity`.
* Full condition: `(rear + 1) % capacity == front`.
* Empty condition: `front == -1`.

**Pseudocode:**

```
procedure enqueue(x):
    if (rear + 1) % capacity == front:
        return "Queue Full"
    if front == -1:
        front = 0
    rear = (rear + 1) % capacity
    arr[rear] = x

procedure dequeue():
    if front == -1:
        return "Queue Empty"
    val = arr[front]
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % capacity
    return val
```

**Complexity:**

* Time: O(1) per operation
* Space: O(n)

---

## 🔹 2. Deque Applications (Sliding Window Maximum)

**Explanation:**
A **Deque (Double-Ended Queue)** allows insertion and deletion from both ends.
Used to optimize sliding window problems (max/min in window).

**Steps (Sliding Window Maximum):**

1. Traverse array with index `i`.
2. Remove indices from back if their value < current element.
3. Remove indices from front if out of window.
4. Front of deque = max of current window.

**Pseudocode:**

```
procedure sliding_window_max(arr, k):
    deque = []
    result = []
    for i in range(n):
        while deque not empty and deque.front() <= i-k:
            deque.pop_front()
        while deque not empty and arr[deque.back()] <= arr[i]:
            deque.pop_back()
        deque.push_back(i)
        if i >= k-1:
            result.append(arr[deque.front()])
    return result
```

**Complexity:**

* Time: O(n)
* Space: O(k)

---

## 🔹 3. LRU Cache (Queue + Hashing)

**Explanation:**
**LRU (Least Recently Used) Cache** keeps the most recently used items and evicts the least recently used when capacity is full.
Implemented using **Doubly Linked List + HashMap** (or OrderedDict in Python).

**Steps:**

* Use a hash map to store key → node reference.
* Doubly linked list maintains usage order:

  * Most recent at head.
  * Least recent at tail.
* On `get`/`put`: move accessed node to head.

**Pseudocode:**

```
class LRUCache:
    init(capacity):
        map = {}
        head, tail = dummy nodes
        connect head <-> tail
        this.capacity = capacity

    get(key):
        if key not in map:
            return -1
        node = map[key]
        move_to_head(node)
        return node.value

    put(key, value):
        if key in map:
            update node value, move_to_head(node)
        else:
            node = new Node(key, value)
            map[key] = node
            add_to_head(node)
            if size > capacity:
                remove tail.prev
```

**Complexity:**

* Get/Put: O(1)
* Space: O(capacity)

---

## 🔹 4. Multi-source BFS (Rotten Oranges type)

**Explanation:**
BFS with **multiple sources** initialized in queue at once.
Applications:

* Rotten Oranges (spread of infection).
* Minimum distance from multiple points.

**Steps:**

1. Push all initial sources into queue with `time=0`.
2. Run BFS, spreading to neighbors.
3. Track maximum time.
4. If unreachable element remains → return -1.

**Pseudocode:**

```
procedure rotten_oranges(grid):
    queue = []
    fresh = 0
    for each cell:
        if cell == rotten:
            queue.push((i, j, 0))
        else if cell == fresh:
            fresh += 1

    time = 0
    while queue not empty:
        i, j, t = queue.pop()
        for each neighbor (x, y):
            if fresh orange:
                fresh -= 1
                grid[x][y] = rotten
                queue.push((x, y, t+1))
        time = max(time, t)

    if fresh > 0:
        return -1
    return time
```

**Complexity:**

* Time: O(m·n)
* Space: O(m·n)

---

## 📊 Comparison Table

| Algorithm                  | Use Case                      | Time   | Space       |
| -------------------------- | ----------------------------- | ------ | ----------- |
| Circular Queue             | Efficient fixed-size queue    | O(1)   | O(n)        |
| Deque (Sliding Window Max) | Max/min in window             | O(n)   | O(k)        |
| LRU Cache                  | Cache with eviction           | O(1)   | O(capacity) |
| Multi-source BFS           | Spread/shortest time problems | O(m·n) | O(m·n)      |

---

## 📂 File Structure

```
Queue_Deque_Algorithms/
├── circular_queue.py
├── deque_sliding_window.py
├── lru_cache.py
├── multi_source_bfs.py
└── README.md
```

---

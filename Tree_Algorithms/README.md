# 📂 `Tree_Algorithms/README.md`

## 📑 Table of Contents

1. [Depth-First Traversals (Preorder, Inorder, Postorder)](#1-depth-first-traversals-preorder-inorder-postorder)
2. [Breadth-First Traversal (Level Order)](#2-breadth-first-traversal-level-order)
3. [Height / Depth of Tree](#3-height--depth-of-tree)
4. [Count Nodes & Leaves](#4-count-nodes--leaves)
5. [Diameter of a Tree](#5-diameter-of-a-tree)
6. [Lowest Common Ancestor](#6-lowest-common-ancestor)
7. [Check Balanced Tree](#7-check-balanced-tree)
8. [Invert / Mirror a Tree](#8-invert--mirror-a-tree)
9. [Validate Binary Search Tree](#9-validate-binary-search-tree)
10. [Kth Smallest / Largest in BST](#10-kth-smallest--largest-in-bst)
11. [Serialize & Deserialize a Tree](#11-serialize--deserialize-a-tree)

---

## 🔹 1. Depth-First Traversals (Preorder, Inorder, Postorder)

**Explanation:**
DFS explores nodes deeply before backtracking.

* **Preorder:** Root → Left → Right
* **Inorder:** Left → Root → Right
* **Postorder:** Left → Right → Root

**Pseudocode (Recursive):**

```
procedure preorder(node):
    if node == null: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

procedure inorder(node):
    if node == null: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

procedure postorder(node):
    if node == null: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```

**Complexity:** O(n) time, O(h) space (h = tree height).

---

## 🔹 2. Breadth-First Traversal (Level Order)

**Explanation:**
Traverse nodes level by level using a queue.

**Pseudocode:**

```
procedure level_order(root):
    if root == null: return
    queue = [root]
    while queue not empty:
        node = queue.pop_front()
        print(node.val)
        if node.left: queue.push(node.left)
        if node.right: queue.push(node.right)
```

**Complexity:** O(n) time, O(n) space.

---

## 🔹 3. Height / Depth of Tree

**Explanation:**
Height = longest path from root to a leaf.

**Recursive Pseudocode:**

```
procedure height(node):
    if node == null: return 0
    return 1 + max(height(node.left), height(node.right))
```

**Complexity:** O(n).

---

## 🔹 4. Count Nodes & Leaves

* **Total nodes:**

```
procedure count_nodes(node):
    if node == null: return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

* **Leaf nodes:**

```
procedure count_leaves(node):
    if node == null: return 0
    if node.left == null and node.right == null: return 1
    return count_leaves(node.left) + count_leaves(node.right)
```

**Complexity:** O(n).

---

## 🔹 5. Diameter of a Tree

**Explanation:**
Diameter = longest path between any two nodes.

**Steps:**

1. At each node, calculate left height + right height.
2. Track max diameter.

**Pseudocode:**

```
procedure diameter(node):
    if node == null: return 0
    left = height(node.left)
    right = height(node.right)
    dia = max(dia, left+right)
    return 1 + max(left, right)
```

**Complexity:** O(n).

---

## 🔹 6. Lowest Common Ancestor (LCA)

**Explanation:**
For nodes `p` and `q`, LCA is the lowest node that has both in its subtree.

**Recursive Pseudocode:**

```
procedure LCA(root, p, q):
    if root == null or root == p or root == q: return root
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if left and right: return root
    return left if left else right
```

**Complexity:** O(n).

---

## 🔹 7. Check Balanced Tree

**Explanation:**
Tree is balanced if height difference of left & right ≤ 1 at every node.

**Pseudocode:**

```
procedure is_balanced(node):
    if node == null: return 0
    left = is_balanced(node.left)
    right = is_balanced(node.right)
    if abs(left - right) > 1: return -1
    return 1 + max(left, right)
```

**Complexity:** O(n).

---

## 🔹 8. Invert / Mirror a Tree

**Explanation:**
Swap left and right subtrees recursively.

**Pseudocode:**

```
procedure invert(node):
    if node == null: return
    swap(node.left, node.right)
    invert(node.left)
    invert(node.right)
```

**Complexity:** O(n).

---

## 🔹 9. Validate Binary Search Tree

**Explanation:**
Check if in-order traversal is strictly increasing.

**Pseudocode:**

```
procedure is_valid_BST(node, min_val, max_val):
    if node == null: return True
    if node.val <= min_val or node.val >= max_val: return False
    return is_valid_BST(node.left, min_val, node.val) and
           is_valid_BST(node.right, node.val, max_val)
```

**Complexity:** O(n).

---

## 🔹 10. Kth Smallest / Largest in BST

**Explanation:**

* Kth smallest → Inorder traversal (ascending).
* Kth largest → Reverse inorder.

**Pseudocode (Kth Smallest):**

```
procedure kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.push(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.right
```

**Complexity:** O(h + k).

---

## 🔹 11. Serialize & Deserialize a Tree

**Explanation:**
Convert tree to string (serialize) and reconstruct it back (deserialize).

**Method:** BFS or DFS with `"null"` for missing nodes.

**Pseudocode (BFS):**

```
procedure serialize(root):
    if root == null: return ""
    queue = [root]
    result = []
    while queue:
        node = queue.pop()
        if node:
            result.append(node.val)
            queue.push(node.left)
            queue.push(node.right)
        else:
            result.append("null")
    return ",".join(result)

procedure deserialize(data):
    if data empty: return null
    values = data.split(",")
    root = new Node(values[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop()
        if values[i] != "null":
            node.left = new Node(values[i])
            queue.push(node.left)
        i += 1
        if values[i] != "null":
            node.right = new Node(values[i])
            queue.push(node.right)
        i += 1
    return root
```

**Complexity:** O(n).

---

## 📊 Comparison Table

| Algorithm                    | Use Case                  | Time   | Space |
| ---------------------------- | ------------------------- | ------ | ----- |
| DFS Traversals               | Root/Left/Right orders    | O(n)   | O(h)  |
| BFS Traversal                | Level order traversal     | O(n)   | O(n)  |
| Height / Depth               | Longest root-to-leaf path | O(n)   | O(h)  |
| Count Nodes & Leaves         | Count total & leaves      | O(n)   | O(h)  |
| Diameter                     | Longest path in tree      | O(n)   | O(h)  |
| Lowest Common Ancestor (LCA) | Common ancestor           | O(n)   | O(h)  |
| Check Balanced Tree          | Balanced height check     | O(n)   | O(h)  |
| Invert / Mirror              | Swap left/right           | O(n)   | O(h)  |
| Validate BST                 | Check BST property        | O(n)   | O(h)  |
| Kth Smallest/Largest in BST  | Order statistics          | O(h+k) | O(h)  |
| Serialize & Deserialize      | Store/restore tree        | O(n)   | O(n)  |

---

## 📂 File Structure

```
Tree_Algorithms/
├── dfs_traversals.py
├── bfs_level_order.py
├── height_depth.py
├── count_nodes_leaves.py
├── diameter.py
├── lowest_common_ancestor.py
├── check_balanced.py
├── invert_tree.py
├── validate_bst.py
├── kth_smallest_largest.py
├── serialize_deserialize.py
└── README.md
```

---

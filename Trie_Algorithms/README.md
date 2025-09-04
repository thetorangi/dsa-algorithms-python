# 📂 `Trie_Algorithms/README.md`

## 📑 Table of Contents

1. [Insert / Search / Delete Word](#1-insert--search--delete-word)
2. [Prefix Matching](#2-prefix-matching)
3. [Word Break Problem (with Trie)](#3-word-break-problem-with-trie)
4. [Autocomplete Feature](#4-autocomplete-feature)

---

## 🔹 1. Insert / Search / Delete Word

**Explanation:**
A **Trie** is a tree-like data structure used for efficient string storage and retrieval, especially for prefixes.

* **Insert:** Add characters one by one, creating nodes if they don’t exist.
* **Search:** Traverse characters; return true if word ends at valid node.
* **Delete:** Mark word as not ending; prune unused nodes if necessary.

**Pseudocode:**

```
class TrieNode:
    children = {}
    end_of_word = False

procedure insert(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = new TrieNode()
        node = node.children[ch]
    node.end_of_word = True

procedure search(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return node.end_of_word

procedure delete(root, word, depth=0):
    if root == null:
        return False
    if depth == len(word):
        if root.end_of_word:
            root.end_of_word = False
        return len(root.children) == 0
    ch = word[depth]
    if ch in root.children and delete(root.children[ch], word, depth+1):
        delete root.children[ch]
        return not root.end_of_word and len(root.children) == 0
    return False
```

**Complexity:**

* Insert: O(L)
* Search: O(L)
* Delete: O(L)
  (where L = length of word).

---

## 🔹 2. Prefix Matching

**Explanation:**
Check if a word starts with a given prefix.

**Steps:**

* Traverse prefix characters in Trie.
* If traversal succeeds → prefix exists.

**Pseudocode:**

```
procedure starts_with(root, prefix):
    node = root
    for ch in prefix:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return True
```

**Complexity:** O(P), where P = prefix length.

---

## 🔹 3. Word Break Problem (with Trie)

**Explanation:**
Given a string and a dictionary, determine if it can be segmented into words from the dictionary.
Trie helps speed up word lookup.

**Steps:**

1. Insert dictionary words into Trie.
2. Use recursion + DP to check if string can be segmented.
3. At each position, traverse Trie until a valid word is found → recurse further.

**Pseudocode:**

```
procedure word_break(s, root, memo, start=0):
    if start == len(s): return True
    if start in memo: return memo[start]
    node = root
    for i from start to len(s)-1:
        if s[i] not in node.children: break
        node = node.children[s[i]]
        if node.end_of_word and word_break(s, root, memo, i+1):
            memo[start] = True
            return True
    memo[start] = False
    return False
```

**Complexity:** O(n²) worst case (n = length of string).

---

## 🔹 4. Autocomplete Feature

**Explanation:**
Given a prefix, return all words in dictionary starting with it.

**Steps:**

1. Traverse Trie until prefix node.
2. DFS from prefix node to collect all words.

**Pseudocode:**

```
procedure autocomplete(root, prefix):
    node = root
    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]
    results = []
    dfs(node, prefix, results)
    return results

procedure dfs(node, path, results):
    if node.end_of_word:
        results.append(path)
    for ch, child in node.children:
        dfs(child, path+ch, results)
```

**Complexity:** O(P + K),

* P = prefix length
* K = number of matching words

---

## 📊 Comparison Table

| Algorithm              | Use Case                   | Time   | Space           |
| ---------------------- | -------------------------- | ------ | --------------- |
| Insert/Search/Delete   | Manage words in dictionary | O(L)   | O(ALPHABET × N) |
| Prefix Matching        | Check prefix existence     | O(P)   | O(1)            |
| Word Break (Trie + DP) | Segment string into words  | O(n²)  | O(n)            |
| Autocomplete           | Suggest words by prefix    | O(P+K) | O(ALPHABET × N) |

---

## 📂 File Structure

```
Trie_Algorithms/
├── insert_search_delete.py
├── prefix_matching.py
├── word_break.py
├── autocomplete.py
└── README.md
```

---

# 📂 `Stack_Algorithms/README.md`

## 📑 Table of Contents

1. [Balanced Parentheses](#1-balanced-parentheses)
2. [Next Greater / Smaller Element](#2-next-greater--smaller-element)
3. [Largest Rectangle in Histogram](#3-largest-rectangle-in-histogram)
4. [Stock Span Problem](#4-stock-span-problem)
5. [Evaluate Postfix Expression](#5-evaluate-postfix-expression)
6. [Infix ↔ Postfix / Prefix Conversion](#6-infix--postfix--prefix-conversion)
7. [Min Stack (Stack with O(1) Minimum)](#7-min-stack-stack-with-o1-minimum)

---

## 🔹 1. Balanced Parentheses

**Explanation:**
Check whether a string containing parentheses/brackets/braces is valid.

**Steps:**

* Traverse string.
* Push opening brackets to stack.
* On closing bracket, check stack top → if mismatch → invalid.
* At the end, stack must be empty.

**Pseudocode:**

```
procedure is_balanced(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mapping.values():
            stack.push(ch)
        else if stack empty or stack.top() != mapping[ch]:
            return False
        else:
            stack.pop()
    return stack empty
```

**Complexity:** O(n) time, O(n) space.

---

## 🔹 2. Next Greater / Smaller Element

**Explanation:**
For each element, find the next element to the right that is greater (or smaller).

**Steps:**

* Traverse array from right to left.
* Maintain a stack of "useful" elements.
* Pop elements not useful (smaller for NGE, larger for NSE).

**Pseudocode (Next Greater):**

```
procedure next_greater(arr):
    stack = []
    result = [-1] * n
    for i from n-1 downto 0:
        while stack not empty and stack.top() <= arr[i]:
            stack.pop()
        if stack not empty:
            result[i] = stack.top()
        stack.push(arr[i])
    return result
```

**Complexity:** O(n) time, O(n) space.

---

## 🔹 3. Largest Rectangle in Histogram

**Explanation:**
Find largest rectangle in histogram bars.
Uses **monotonic stack** to find nearest smaller elements on both sides.

**Steps:**

1. For each bar, find `next smaller to left` and `next smaller to right`.
2. Width = `right[i] - left[i] - 1`.
3. Area = `height[i] * width`.
4. Track max area.

**Complexity:** O(n) time, O(n) space.

---

## 🔹 4. Stock Span Problem

**Explanation:**
For each day, find how many consecutive previous days had stock prices ≤ today’s price.

**Steps:**

* Use a monotonic stack storing `(price, index)`.
* While top ≤ current price, pop.
* Span = current\_index – previous\_greater\_index.

**Pseudocode:**

```
procedure stock_span(prices):
    stack = []
    span = []
    for i in range(n):
        while stack not empty and stack.top().price <= prices[i]:
            stack.pop()
        if stack empty:
            span[i] = i+1
        else:
            span[i] = i - stack.top().index
        stack.push((prices[i], i))
    return span
```

**Complexity:** O(n) time, O(n) space.

---

## 🔹 5. Evaluate Postfix Expression

**Explanation:**
Evaluate expression given in **postfix notation (Reverse Polish Notation)**.

**Steps:**

1. Traverse tokens left to right.
2. If operand → push to stack.
3. If operator → pop 2 operands, apply operation, push result back.
4. Final element in stack = answer.

**Pseudocode:**

```
procedure eval_postfix(expr):
    stack = []
    for token in expr:
        if token is number:
            stack.push(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.push(apply_operator(a, b, token))
    return stack.top()
```

**Complexity:** O(n) time, O(n) space.

---

## 🔹 6. Infix ↔ Postfix / Prefix Conversion

**Explanation:**
Convert between infix, postfix, and prefix using **operator precedence** and **stack**.

* **Infix → Postfix (Shunting Yard Algorithm):**

  * If operand → output.
  * If operator → pop operators with higher precedence from stack, then push.
  * If `(` → push to stack.
  * If `)` → pop until `(`.

* **Postfix → Infix:** Use stack to build expression trees.

**Complexity:** O(n) time, O(n) space.

---

## 🔹 7. Min Stack (Stack with O(1) Minimum)

**Explanation:**
Support `push`, `pop`, and `getMin` in O(1).

**Steps:**

* Maintain 2 stacks:

  * `mainStack` stores all values.
  * `minStack` stores minimum at each level.

**Pseudocode:**

```
procedure push(x):
    main.push(x)
    if minStack empty or x <= minStack.top():
        minStack.push(x)

procedure pop():
    if main.top() == minStack.top():
        minStack.pop()
    main.pop()

procedure getMin():
    return minStack.top()
```

**Complexity:** O(1) per operation.

---

## 📊 Comparison Table

| Algorithm                         | Use Case                     | Time | Space |
| --------------------------------- | ---------------------------- | ---- | ----- |
| Balanced Parentheses              | Check valid brackets         | O(n) | O(n)  |
| Next Greater / Smaller Element    | Find nearest greater/smaller | O(n) | O(n)  |
| Largest Rectangle in Histogram    | Max area in histogram        | O(n) | O(n)  |
| Stock Span Problem                | Stock price span             | O(n) | O(n)  |
| Evaluate Postfix Expression       | Expression evaluation        | O(n) | O(n)  |
| Infix ↔ Postfix/Prefix Conversion | Expression conversion        | O(n) | O(n)  |
| Min Stack                         | Stack with O(1) min          | O(1) | O(n)  |

---

## 📂 File Structure

```
Stack_Algorithms/
├── balanced_parentheses.py
├── next_greater_smaller.py
├── largest_histogram.py
├── stock_span.py
├── evaluate_postfix.py
├── infix_postfix_prefix.py
├── min_stack.py
└── README.md
```

---

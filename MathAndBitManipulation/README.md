# 📂 `MathAndBitManipulation/README.md`

## 📑 Table of Contents

1. [Greatest Common Divisor (GCD) & Least Common Multiple (LCM)](#1-greatest-common-divisor-gcd--least-common-multiple-lcm)
2. [Sieve of Eratosthenes (Prime Generation)](#2-sieve-of-eratosthenes-prime-generation)
3. [Modular Exponentiation (Fast Power)](#3-modular-exponentiation-fast-power)
4. [Modular Inverse (Fermat’s Little Theorem)](#4-modular-inverse-fermats-little-theorem)
5. [Fast Doubling Fibonacci](#5-fast-doubling-fibonacci)
6. [Count Set Bits (Brian Kernighan’s Algorithm)](#6-count-set-bits-brian-kernighans-algorithm)
7. [Check Power of Two](#7-check-power-of-two)
8. [XOR Tricks (Missing Number, Single Number, etc.)](#8-xor-tricks-missing-number-single-number-etc)
9. [Bitmasking (Subsets, DP, Optimization)](#9-bitmasking-subsets-dp-optimization)

---

## 🔹 1. Greatest Common Divisor (GCD) & Least Common Multiple (LCM)

**Explanation:**

* GCD via **Euclidean Algorithm**.
* LCM via formula: `LCM(a, b) = (a * b) / GCD(a, b)`.

**Complexity:**

* O(log(min(a, b))).

---

## 🔹 2. Sieve of Eratosthenes (Prime Generation)

**Explanation:**

* Mark multiples of primes as non-prime.
* Generates all primes up to N efficiently.

**Complexity:**

* Time: O(N log log N)
* Space: O(N)

---

## 🔹 3. Modular Exponentiation (Fast Power)

**Explanation:**

* Computes (a^b) % m using exponentiation by squaring.

**Complexity:**

* Time: O(log b)

---

## 🔹 4. Modular Inverse (Fermat’s Little Theorem)

**Explanation:**

* If m is prime, inverse of `a` under modulo m is `a^(m-2) % m`.

**Complexity:**

* Time: O(log m)

---

## 🔹 5. Fast Doubling Fibonacci

**Explanation:**

* Computes Fibonacci in O(log n) using recurrence:

  * F(2k) = F(k) \* \[2\*F(k+1) − F(k)]
  * F(2k+1) = F(k+1)^2 + F(k)^2

---

## 🔹 6. Count Set Bits (Brian Kernighan’s Algorithm)

**Explanation:**

* Repeatedly turn off the lowest set bit using `n = n & (n-1)`.

**Complexity:**

* O(number of set bits).

---

## 🔹 7. Check Power of Two

**Explanation:**

* A number is power of 2 if `n > 0 and (n & (n-1)) == 0`.

**Complexity:**

* O(1).

---

## 🔹 8. XOR Tricks (Missing Number, Single Number, etc.)

**Examples:**

* Find missing number: XOR all numbers 1…n and given array.
* Find element occurring once while others occur twice: XOR all elements.

**Complexity:**

* O(n).

---

## 🔹 9. Bitmasking (Subsets, DP, Optimization)

**Explanation:**

* Use integer bits to represent subsets.
* Useful in DP problems (TSP, subset sum).

**Complexity:**

* Generates all subsets in O(2^n).

---

## 📊 Comparison Table

| Algorithm               | Use Case              | Time           | Space |
| ----------------------- | --------------------- | -------------- | ----- |
| GCD & LCM               | Number theory         | O(log n)       | O(1)  |
| Sieve of Eratosthenes   | Prime generation      | O(N log log N) | O(N)  |
| Modular Exponentiation  | Fast power mod        | O(log n)       | O(1)  |
| Modular Inverse         | Division mod prime    | O(log n)       | O(1)  |
| Fast Doubling Fibonacci | Fibonacci mod         | O(log n)       | O(1)  |
| Count Set Bits          | Bit tricks            | O(set bits)    | O(1)  |
| Check Power of Two      | Validation            | O(1)           | O(1)  |
| XOR Tricks              | Missing/single number | O(n)           | O(1)  |
| Bitmasking              | Subsets, DP           | O(2^n)         | O(1)  |

---

## 📂 File Structure

```
MathAndBitManipulation/
├── gcd_lcm.py
├── sieve_of_eratosthenes.py
├── modular_exponentiation.py
├── modular_inverse.py
├── fast_doubling_fibonacci.py
├── count_set_bits.py
├── check_power_of_two.py
├── xor_tricks.py
├── bitmasking.py
└── README.md
```

---

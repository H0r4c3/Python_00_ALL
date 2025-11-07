'''
Recurrence in Python typically refers to recursion—a process where a function calls itself to solve smaller instances of the same problem. It's a fundamental concept in programming and mathematics, often used to solve problems that can be broken down into smaller subproblems.

Here's a quick guide to using recurrence (recursion) in Python:
'''

'1. Factorial Example'

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


'2. Fibonacci Sequence'

'''

'''

def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

'3. General Recurrence Relations'

def recurrence(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return recurrence(n - 1) + 2 * n

print(recurrence(5))  # Output: 31


'''
Optimizing Recursion with Memoization
To avoid redundant calculations, use a cache (e.g., a dictionary or the functools.lru_cache decorator):
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_optimized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)

print(fibonacci_optimized(50))  # Output: 12586269025


'''
Recurrence in Python typically refers to **recursion**—a process where a function calls itself to solve smaller instances of the same problem. It's a fundamental concept in programming and mathematics, often used to solve problems that can be broken down into smaller subproblems.

Here's a quick guide to using recurrence (recursion) in Python:

---

### 1. **Factorial Example**

The factorial of a number \( n \) (denoted \( n! \)) is defined recursively:
\[
n! = n \times (n-1)!
\]
with the base case \( 0! = 1 \).

```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### 2. **Fibonacci Sequence**

The Fibonacci sequence is defined as:
\[
F(n) = F(n-1) + F(n-2)
\]
with the base cases \( F(0) = 0 \) and \( F(1) = 1 \).

```python
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

---

### 3. **General Recurrence Relations**

You can implement any recurrence relation by defining a base case and a recursive step. For example, solving \( a(n) = a(n-1) + 2n \) with \( a(0) = 1 \):

```python
def recurrence(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return recurrence(n - 1) + 2 * n

print(recurrence(5))  # Output: 31
```

---

### Key Points:
- **Base Case:** Prevents infinite recursion by providing a stopping point.
- **Recursive Case:** Solves smaller subproblems and combines their results.
- **Efficiency:** Recursive solutions can sometimes be slow due to repeated computations (e.g., naive Fibonacci). You can optimize with techniques like **memoization** or **dynamic programming**.

---

### Optimizing Recursion with Memoization
To avoid redundant calculations, use a cache (e.g., a dictionary or the `functools.lru_cache` decorator):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_optimized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)

print(fibonacci_optimized(50))  # Output: 12586269025
```
'''
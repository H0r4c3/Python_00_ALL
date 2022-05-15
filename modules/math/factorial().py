'https://realpython.com/lessons/python-math-module-overview/'

import math
import timeit

# using 'factorial' function from 'math' module
n = 6
print(math.factorial(n))


# Using for loop
def fact_loop(num):

    if num < 0 or not isinstance(num, int):
        raise ValueError("num must be a positive integer")
    
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = i * factorial

    return factorial

print(fact_loop(n))

# Using recursion
def fact_recursion(num):

    if num < 0 or not isinstance(num, int):
        raise ValueError("num must be a positive integer")

    if num == 0:
        return 1

    return num * fact_recursion(num - 1)

print(fact_recursion(n))

with_loop = timeit.timeit("fact_loop(10)", globals=globals())

with_recursion = timeit.timeit("fact_recursion(10)", globals=globals())

with_factorial = timeit.timeit("math.factorial(10)", globals=globals())

print('with_loop =', with_loop)
print('with_recursion =', with_recursion)
print('with_factorial =', with_factorial)
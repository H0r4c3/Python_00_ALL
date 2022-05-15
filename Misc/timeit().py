'https://docs.python.org/3/library/timeit.html'

# testing timeit module

import timeit
import time
#import sys


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

#print(sys.getrecursionlimit())

starttime = time.perf_counter()
print("The start time is :", starttime)
print(f'Result = {factorial(500)}')
print("The end time is :", time.perf_counter())
print("The time difference is :", time.perf_counter() - starttime)


# time for 500.000 calculations
my_time = timeit.timeit("factorial(6)", number = 500_000, globals = globals())
print(f'factorial(6) repeated 500_000 times = {my_time} seconds')


# create a function for elapsed time
def elapsed_time(my_function):
    my_time = timeit.timeit(my_function, number=500_000, globals=globals())
    return f'{my_time:.3f} seconds'

print(elapsed_time('factorial(6)'))
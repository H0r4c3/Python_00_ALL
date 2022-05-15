'https://docs.python.org/3/library/timeit.html'

# testing timeit()

import timeit


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


starttime = timeit.default_timer()
print("The start time is :", starttime)
print(f'Result = {factorial(1000)}')
print("The end time is :", timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)

'https://glowingpython.blogspot.com/2019/03/speeding-up-sieve-of-eratosthenes-with.html'
'''
Lessons learned:
Using Numba is very straightforward and a Python function written in a decent manner can be speeded up with little effort.
Python lists are too heavy in some cases. Even with pre-allocation of the memory they can't beat Numpy arrays for this specific task.
Assigning types correctly is key. Using a Numpy array of integers instead of bools in the function sieve_numpy_jit would result in a slow down.
'''

# Here's the first version of the implementation

def sieve_python(limit):
    is_prime = [True]*limit
    is_prime[0] = False
    is_prime[1] = False
    for d in range(2, int(limit**0.5) + 1):
        if is_prime[d]:
            for n in range(d*d, limit, d):
                is_prime[n] = False  
    return is_prime

# I decided to time it:
from timeit import timeit

def elapse_time(s):
    s = timeit(s, number=100, globals=globals())
    return f'{s:.3f} seconds'

print(elapse_time('sieve_python(100000)'))



# # The only addition to the previous version is the decorator @njit and this simple change resulted in a whopping 10x speed up! 
# # 0.103 seconds
# from numba import njit

# @njit
# def sieve_python_jit(limit):
#     is_prime = [True]*limit
#     is_prime[0] = False
#     is_prime[1] = False
#     for d in range(2, int(limit**0.5) + 1):
#         if is_prime[d]:
#             for n in range(d*d, limit, d):
#                 is_prime[n] = False  
#     return is_prime

# sieve_python_jit(10) # compilation
# print(elapse_time('sieve_python_jit(100000)'))




# # Combining Numba with the appropriate Numpy data structures leads to impressive results
# # 0.018 seconds
# import numpy as np

# @njit
# def sieve_numpy_jit(limit):
#     is_prime = np.full(limit, True)
#     is_prime[0] = False
#     is_prime[1] = False
#     for d in range(2, int(np.sqrt(limit) + 1)):
#         if is_prime[d]:
#             for n in range(d*d, limit, d):
#                 is_prime[n] = False  
#     return is_prime

# sieve_numpy_jit(10) # compilation
# print(elapse_time('sieve_numpy_jit(100000)'))



# I thought the implementation seemed kinda slow without numba, so i gave it a shot with a pure numpy implementation.
# https://www.reddit.com/r/Python/comments/b6j9pn/speeding_up_the_sieve_of_eratosthenes_with_numba/

import numpy as np

def sieve_python_np(limit):
    if limit < 2: return np.array([])
    if limit < 3: return np.array([2])
    is_prime = np.ones(limit+1, dtype=np.bool_)
    is_prime[4 : : 2] = 0
    for d in range(3, int(np.sqrt(limit))+1, 2):
        if is_prime[d]:
            is_prime[d*d::d] = 0
    return np.nonzero(is_prime)[0][2:]

print(elapse_time('sieve_python_np(100000)'))
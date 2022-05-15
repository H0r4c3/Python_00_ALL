'https://blog.finxter.com/numpy-np-diff-simply-explained-bonus-video/'

'''
NumPy’s np.diff() function calculates the difference between subsequent values in a NumPy array. 
For example, np.diff([1, 2, 4]) returns the difference array [1 2].

By defining the argument n, you can execute the diff function multiple times on the respective output of the last execution. 
Hence, the call np.diff(x, n=2) results in the same output as np.diff(np.diff(x)).
'''

import numpy as np

# 1. Example
# Fibonacci Sequence with first 8 numbers
fibs = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21])

diff_fibs = np.diff(fibs)
print(diff_fibs) # -> [1 0 1 1 2 3 5 8]


# 2. Example
a = np.array([[0, 1, 1],
              [2, 3, 5],
              [8, 13, 21]])
diffs = np.diff(a, axis=1)
print(diffs)
"""
[[1 0]
 [1 2]
 [5 8]]
"""


# 3. Example
a = np.array([2, 4, 7, 4, 1, 8, 11, 12])
print(np.diff(a, n=1)) # -> [ 2  3 -3 -3  7  3  1]
print(np.diff(a, n=2)) # -> [ 1 -6  0 10 -4 -2]
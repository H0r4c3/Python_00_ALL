'https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html'

'''
Find the indices of array elements that are non-zero, grouped by element.
'''

import numpy as np

my_arr = np.array([[2, 0, 0], [1, 0, 0], [5, 0, 0]])
print(my_arr)
print(my_arr.nonzero())
print(np.argwhere(my_arr>0))
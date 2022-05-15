'https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html'
'https://www.journaldev.com/32797/python-convert-numpy-array-to-list'

'''
Return the array as an a.ndim-levels deep nested list of Python scalars.

Return a copy of the array data as a (nested) Python list. 
Data items are converted to the nearest compatible builtin Python type, via the item function.
'''

import numpy as np

# 2d array to list
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f'NumPy Array:\n{arr}')

list1 = arr.tolist()

print(f'List: {list1}')
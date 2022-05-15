'https://www.w3schools.com/python/numpy/numpy_array_shape.asp'

'''
The shape of an array is the number of elements in each dimension.
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

'''

# Print the shape of a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
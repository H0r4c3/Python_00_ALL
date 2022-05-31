'https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html'

'''
Return the indices of the elements that are non-zero.

Returns a tuple of arrays, one for each dimension of a, containing the indices of the non-zero elements in that dimension. 
The values in a are always tested and returned in row-major, C-style order.

To group the indices by element, rather than dimension, use 'argwhere', which returns a row for each non-zero element.
'''
import numpy as np

my_arr = np.array([[2, 0, 0], [1, 0, 0], [5, 0, 0]])
print(my_arr)
print(my_arr.nonzero())
print(np.argwhere(my_arr>0).tolist())
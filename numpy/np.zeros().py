'https://numpy.org/doc/stable/reference/generated/numpy.zeros.html'

'''
numpy.zeros(shape, dtype=float, order='C', *, like=None)
Return a new array of given shape and type, filled with zeros.

Parameters
shapeint or tuple of ints
Shape of the new array, e.g., (2, 3) or 2.

dtype data-type, optional
The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.

order{‘C’, ‘F’}, optional, default: ‘C’
Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

likearray_like
Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as like supports the __array_function__ protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns
out ndarray
Array of zeros with the given shape, dtype, and order.
'''
import numpy as np

s = (4, 4)
my_arr = np.zeros(s, dtype = int)
print(my_arr)

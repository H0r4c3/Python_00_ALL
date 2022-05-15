'https://numpy.org/devdocs/reference/generated/numpy.eye.html'

'''
numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)[source]
Return a 2-D array with ones on the diagonal and zeros elsewhere.

Parameters
N int
Number of rows in the output.

Mint, optional
Number of columns in the output. If None, defaults to N.

k int, optional
Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.

dtype data-type, optional
Data-type of the returned array.

order{‘C’, ‘F’}, optional
Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory.

New in version 1.14.0.

likearray_like
Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as like supports the __array_function__ protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns
Indarray of shape (N,M)
An array where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.
'''

import numpy as np

print(np.eye(5, dtype=int))

print(np.eye(3, k=1))
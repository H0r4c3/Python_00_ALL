'https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html'
'https://www.pythonpool.com/numpy-count_nonzero/'

'''
numpy.count_nonzero(a, axis=None, *, keepdims=False)[source]
Counts the number of non-zero values in the array a.

Parameters
a : array_like
The array for which to count non-zeros.

axis : int or tuple, optional
Axis or tuple of axes along which to count non-zeros. Default is None, meaning that non-zeros will be counted along a flattened version of a.

keepdims : bool, optional
If this is set to True, the axes that are counted are left in the result as dimensions with size one. With this option, 
the result will broadcast correctly against the input array.

Returns
countint or array of int
Number of non-zero values in the array along a given axis. Otherwise, the total number of non-zero values in the array is returned.
'''

import numpy as np
a = [[0, 1, 7, 0], [3, 0, 2, 19]]

# 1. Example
print(np.count_nonzero(a))
print(np.count_nonzero(a, axis=0)) # array([1, 1, 2, 1])
print(np.count_nonzero(a, axis=1)) # array([2, 3])
print(np.count_nonzero(a, axis=1, keepdims=True))


# 2. Example
grille_arr = np.array([['.', '.', 'X', '.'],
 ['.', '.', '.', '.'],
 ['X', 'X', '.', '.'],
 ['.', '.', '.', 'X']])

print(grille_arr)

c = np.count_nonzero(grille_arr == 'X')
print(c)

# 3. Example
arr = np.eye(5, dtype=int)
print(arr)

c = np.count_nonzero(arr)
print(c)
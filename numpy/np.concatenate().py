'https://www.w3schools.com/python/numpy/numpy_array_join.asp'
'https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html'

'''
We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

numpy.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
'''


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.stack((arr1, arr2), axis=1)
print(arr)


# Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
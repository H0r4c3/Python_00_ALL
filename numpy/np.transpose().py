'https://numpy.org/doc/stable/reference/generated/numpy.transpose.html'

'''
Reverse or permute the axes of an array; returns the modified array.

For an array a with two axes, transpose(a) gives the matrix transpose.
'''

import numpy as np

np_arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(np_arr)

np_arr2 = np.reshape(np_arr, (2, 4))
print(np_arr2)

my_arr = np.array([[0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]])
print(my_arr)
np_arr3 = np.transpose(my_arr)
print(np_arr3)

# another syntax of transpose() method
np_arr3_bis = my_arr.transpose()
print(np_arr3_bis)

np_arr4 = np_arr3.flatten()
print(np_arr4)
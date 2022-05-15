'https://www.geeksforgeeks.org/numpy-reshape-python/'

'''
The numpy.reshape() function shapes an array without changing the data of the array.
 

Syntax: numpy.reshape(array, shape, order = 'C')
Parameters : 

array : [array_like]Input array
shape : [int or tuples of int] e.g. if we are aranging an array with 10 elements then shaping
        it like numpy.reshape(4, 8) is wrong; we can 
order  : [C-contiguous, F-contiguous, A-contiguous; optional]         
         C-contiguous order in memory(last index varies the fastest)
         C order means that operating row-rise on the array will be slightly quicker
         FORTRAN-contiguous order in memory (first index varies the fastest).
         F order means that column-wise operations will be faster. 
         ‘A’ means to read / write the elements in Fortran-like index order if,
         array is Fortran contiguous in memory, C-like order otherwise
Return : 

Array which is reshaped without changing the data.
'''


import numpy as np

np_arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(np_arr)

np_arr_2 = np.reshape(np_arr, (2, 4))
print(np_arr_2)

np_arr_22 = np_arr.reshape(2, 4)
print(np_arr_22)

# One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions.
np_arr_3 = np.reshape(np_arr, (2, -1))
print(np_arr_3)


#Convert the array into a 1D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
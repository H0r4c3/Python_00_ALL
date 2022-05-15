'https://www.geeksforgeeks.org/numpy-sum-in-python/'

'''
numpy.sum(arr, axis, dtype, out) : This function returns the sum of array elements over the specified axis.

Parameters :
arr : input array.
axis : axis along which we want to calculate the sum value. Otherwise, it will consider arr to be flattened(works on all the axis). axis = 0 means along the column and axis = 1 means working along the row.
out : Different array in which we want to place the result. The array must have same dimensions as expected output. Default is None.
initial : [scalar, optional] Starting value of the sum.

Return : Sum of the array elements (a scalar value if axis is none) or array with sum values along the specified axis.
'''


import numpy as np 
       
# 2D array 
arr = [[1, 2, 3, 4, 5],   
       [1, 2, 3, 4, 5],  
       [1, 2, 3, 4, 5,]] 

print("\nSum of arr : ", np.sum(arr)) 
print("Sum of arr(axis = 0) : ", np.sum(arr, axis = 0)) 
print("Sum of arr(axis = 1) : ", np.sum(arr, axis = 1))
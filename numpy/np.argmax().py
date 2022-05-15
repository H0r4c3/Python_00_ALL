'https://www.geeksforgeeks.org/numpy-argmax-python/'

'''
The numpy.argmax() function returns INDICES (!!!!!!) of the max element of the array in a particular axis. 

Syntax : 
numpy.argmax(array, axis = None, out = None)

Parameters : 

array : Input array to work on 
axis  : [int, optional]Along a specified axis like 0 or 1
out   : [array optional]Provides a feature to insert output to the out
          array and it should be of appropriate shape and dtype
          
Return :
Array of indices into the array with same shape as array.shape
 with the dimension along axis removed.
'''

import numpy as np
arr = [[1, 5, 3, 10, 4],   
       [6, 7, 8, 9, 8],  
       [11, 2, 13, 4, 15]]

# No axis mentioned, so works on entire array
print("\nMax element : ", np.argmax(arr))
 
# returning Indices of the max element
# as per the indices
print("\nIndices of Max element : ", np.argmax(arr, axis=0))
print("\nIndices of Max element : ", np.argmax(arr, axis=1))
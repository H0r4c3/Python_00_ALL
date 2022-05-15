'''
https://www.geeksforgeeks.org/find-common-values-between-two-numpy-arrays/

In NumPy, we can find common values between two arrays with the help intersect1d(). 
It will take parameter two arrays and it will return an array in which all the common elements will appear.

Syntax: numpy.intersect1d(array1,array2)
Return :An array in which all the common element will appear.
'''

import numpy as np

ar1 = np.array([0, 1, 2, 3, 4])
ar2 = [1, 3, 4]
  
# Common values between two arrays
print(np.intersect1d(ar1, ar2))
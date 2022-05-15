'https://www.geeksforgeeks.org/numpy-linalg-det-method-in-python/'

'''
In NumPy, we can compute the determinant of the given square array with the help of numpy.linalg.det(). 
It will take the given square array as a parameter and return the determinant of that.

Syntax: numpy.linalg.det() 
Parameter: An square array. 
Return: The determinant of that square array
'''

import numpy as np
 
# 1. Example
array1 = np.array([[1, 2], [3, 4]])
 
# Original 2-d array
print(array1)
 
# Determinant of the said 2-D array
print(np.linalg.det(array1))
      
      
 
# 2. Example
array1 = np.array([[1, 2, 3], [3, 4, 1], [3, 2, 1]])
 
# Original 2-d array
print(array1)
 
# Determinant of the said 2-D array
print(np.linalg.det(array1))
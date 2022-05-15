'https://www.tutorialsandyou.com/python/numpy-max-in-python-39.html'

'''
Numpy max() function is used to get a maximum value along a specified axis.

Syntax of Numpy.max()
np.max(a, axis=None)
a parameter refers to the array on which you want to apply np.max() function.

axis parameter is optional and helps us to specify the axis on which we want to find the maximum values.
When axis=0 is passed to max() function, then max in every COLUMN is selected
When axis=1 is passed to max() function, then max in every ROW is selected
'''

import numpy as np
 
a = np.array([[50, 15, 89, 23, 64], 
              [45, 98, 25, 17, 55], 
              [35, 37, 9, 100, 61]])
print('Maximum value in arr: ', np.max(a))
print('Maximum value in arr along axis 0: ', np.max(a, axis=0)) # max in every COLUMN
print('Maximum value in arr along axis 1: ', np.max(a, axis=1)) # max in every ROW
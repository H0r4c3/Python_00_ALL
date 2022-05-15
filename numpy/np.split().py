'https://www.tutorialspoint.com/numpy/numpy_split.htm'

'''
This function divides the array into subarrays along a specified axis. The function takes three parameters.

numpy.split(ary, indices_or_sections, axis)

ary = Input array to be split

indices_or_sections = Can be an integer, indicating the number of equal sized subarrays to be created from the input array. 
If this parameter is a 1-D array, the entries indicate the points at which a new subarray is to be created.

axis = Default is 0
'''

import numpy as np 
a = np.arange(9)

print(a)

print('Split the array in 3 equal-sized subarrays:') 
b = np.split(a, 3) 
print(b)   

print('Split the array at positions indicated in 1-D array:') 
b = np.split(a, [4, 7])
print(b) 


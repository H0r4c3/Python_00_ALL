'https://www.geeksforgeeks.org/numpy-delete-python/'

'''
The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis. 

numpy.delete(array, object, axis = None)

Parameters:
array   : [array_like]Input array. 
object  : [int, array of ints]Sub-array to delete
axis    : Axis along which we want to delete sub-arrays. By default, it object is applied to  flattened array
'''

import numpy as np

my_list = [0, 11, 12, 13, 14, 15, 16, 17, 18]
result = np.delete(my_list, [1, 3, 5, 7])
print(list(result))
'https://www.udemy.com/course/numpy-for-scientific-computation-with-python/learn/lecture/28151502#overview'

import numpy as np

num_array = np.array([1, 2, 3, 4])
print(num_array)

num_array = np.array((1, 2, 3, 4), dtype=float)
print(num_array)

num_array = np.array((1, 2, 3, 4), dtype=str)
print(num_array)


dict = {1:'one', 2:'two', 3:'three'}
data = list(dict.items())
data = dict.fromkeys(data)
print(f'data = {data}')
num_array = np.array(data)
print(num_array)


'https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp'

# Create an array with 5 dimensions and verify that it has 5 dimensions:

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

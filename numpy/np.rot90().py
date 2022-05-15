'https://numpy.org/doc/stable/reference/generated/numpy.rot90.html'
'https://www.geeksforgeeks.org/numpy-rot90-python/'

'''
numpy.rot90(m, k=1, axes=(0, 1))[source]
Rotate an array by 90 degrees in the plane specified by axes.

Rotation direction is from the first towards the second axis.

Parameters
m: array_like
Array of two or more dimensions.

k: integer
Number of times the array is rotated by 90 degrees.

axes: (2,) array_like
The array is rotated in the plane defined by the axes. Axes must be different.

Returns
y: ndarray
A rotated view of m.
'''

import numpy as np
m = np.array([[1,2],[3,4]], int)
print(m)
print(np.rot90(m)) # 1 = counterclockwise
print(np.rot90(m, 2)) # 2
print(np.rot90(m, 3))
print(np.rot90(m, 4)) # back to start

print(np.rot90(m, 1, (0,1))) # same as 1
print(np.rot90(m, 1, (1,0))) # clockwise 
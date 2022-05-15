'https://www.w3schools.com/python/numpy/numpy_array_iterating.asp'

'''
The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration, lets go through it with examples.

Iterating on Each Scalar Element
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
'''

#Iterate through the following 3-D array:

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
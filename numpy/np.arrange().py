'https://www.geeksforgeeks.org/numpy-arrange-in-python/'

'''
The arrange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. 
The interval mentioned is half-opened i.e. [Start, Stop) 

Parameters : 

start : [optional] start of interval range. By default start = 0
stop  : end of interval range
step  : [optional] step size of interval. By default step size = 1,  
For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
dtype : type of output array
Return: 

Array of evenly spaced values.
Length of array being generated  = Ceil((Stop - Start) / Step) 
'''

import numpy as np

print(np.arange(4), "\n")
  
print(np.arange(4, 10), "\n")
  
print(np.arange(4, 20, 3), "\n")
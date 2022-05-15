'https://www.geeksforgeeks.org/flatten-a-matrix-in-python-using-numpy/'

'''
By using ndarray.flatten() function we can flatten a matrix to one dimension in python.

Syntax:numpy_array.flatten(order=’C’)

order:‘C’ means to flatten in row-major.’F’ means to flatten in column-major.’A’ means to flatten in column-major order if a is Fortran contiguous in memory, 
row-major order otherwise.’K’ means to flatten a in the order the elements occur in memory. The default is ‘C’.
Return:Flattened 1-D matrix
'''

# importing numpy as np
import numpy as np
  
# declare matrix with np
gfg = np.array([[2, 3], [4, 5]])
  
# using array.flatten() method
flat_gfg = gfg.flatten()
print(flat_gfg)
'https://numpy.org/doc/stable/reference/generated/numpy.ix_.html'

'''
numpy.ix_(*args)[source]
Construct an open mesh from multiple sequences.

This function takes N 1-D sequences and returns N outputs with N dimensions each, such that the shape is 1 in all but one dimension and 
the dimension with the non-unit shape value cycles through all N dimensions.

Using ix_ one can quickly construct index arrays that will index the cross product. a[np.ix_([1,3],[2,5])] returns the array [[a[1,2] a[1,5]], [a[3,2] a[3,5]]].

Parameters
args1-D sequences
Each sequence should be of integer or boolean type. Boolean sequences will be interpreted as boolean masks for the corresponding 
dimension (equivalent to passing in np.nonzero(boolean_sequence)).

Returns
outtuple of ndarrays
N arrays with N dimensions each, with N the number of input sequences. Together these arrays form an open mesh.
'''
import numpy as np

my_arr = np.array([[0, 1, 2, 3, 4],
                   [5, 6, 7, 8, 9], 
                   [10, 11, 12, 13, 14]])

print(my_arr)

selection = np.ix_([0, 1, 2], [0, 1, 2, 3]) # select rows nr. 0, 1, 2 and columns nr. 0, 1, 2, 3, 4
sub_arr1 = my_arr[selection]
print(sub_arr1)

# Same result using slice
print(my_arr[0:3, 0:4])
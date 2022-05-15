'https://numpy.org/doc/stable/reference/generated/numpy.flip.html'

'''
numpy.flip(m, axis=None)[source]
Reverse the order of elements in an array along the given axis.

The shape of the array is preserved, but the elements are reordered.

New in version 1.12.0.

Parameters
m : array_like
Input array.

axisNone or int or tuple of ints, optional
Axis or axes along which to flip over. The default, axis=None, will flip over all of the axes of the input array. If axis is negative it counts from the last to the first axis.

If axis is a tuple of ints, flipping is performed on all of the axes specified in the tuple.

Changed in version 1.15.0: None and tuples of axes are supported

Returns
outarray_like
A view of m with the entries of axis reversed. Since a view is returned, this operation is done in constant time.
'''

import numpy as np

old_array = np.array([[1, 2, 3], [4, 5, 6]])
print(old_array)

flipped_array = np.flip(old_array)
print(flipped_array)

flipped_vertically_array = np.flip(old_array, axis=0)
print(flipped_vertically_array)

flipped_horizontally_array = np.flip(old_array, axis=1)
print(flipped_horizontally_array)
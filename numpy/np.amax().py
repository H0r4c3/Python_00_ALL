'https://numpy.org/doc/stable/reference/generated/numpy.amax.html'

'''
numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)[source]
Return the maximum of an array or maximum along an axis.

Parameters
aarray_like
Input data.

axisNone or int or tuple of ints, optional
Axis or axes along which to operate. By default, flattened input is used.

New in version 1.7.0.

If this is a tuple of ints, the maximum is selected over multiple axes, instead of a single axis or all the axes as before.

outndarray, optional
Alternative output array in which to place the result. Must be of the same shape and buffer length as the expected output. See Output type determination for more details.

keepdimsbool, optional
If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then keepdims will not be passed through to the amax method of sub-classes of ndarray, however any non-default value will be. If the sub-class’ method does not implement keepdims any exceptions will be raised.

initialscalar, optional
The minimum value of an output element. Must be present to allow computation on empty slice. See reduce for details.

New in version 1.15.0.

wherearray_like of bool, optional
Elements to compare for the maximum. See reduce for details.

New in version 1.17.0.

Returns
amaxndarray or scalar
Maximum of a. If axis is None, the result is a scalar value. If axis is given, the result is an array of dimension a.ndim - 1.
'''
import numpy as np
a = np.arange(4).reshape((2,2))
print(a)

a = np.array([[10, 1, 2],
            [3, 4, 5]])
print(np.amax(a))
print(np.amax(a, axis=0))
print(np.amax(a, axis=1))
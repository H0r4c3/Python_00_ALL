'https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html'

'''
ndarray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
Copy of the array, cast to a specified type.

Parameters
dtypestr or dtype
Typecode or data-type to which the array is cast.

order{‘C’, ‘F’, ‘A’, ‘K’}, optional
Controls the memory layout order of the result. ‘C’ means C order, ‘F’ means Fortran order, ‘A’ means ‘F’ order if all the arrays are Fortran contiguous, ‘C’ order otherwise, and ‘K’ means as close to the order the array elements appear in memory as possible. Default is ‘K’.

casting{‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
Controls what kind of data casting may occur. Defaults to ‘unsafe’ for backwards compatibility.

‘no’ means the data types should not be cast at all.

‘equiv’ means only byte-order changes are allowed.

‘safe’ means only casts which can preserve values are allowed.

‘same_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.

‘unsafe’ means any data conversions may be done.

subokbool, optional
If True, then sub-classes will be passed-through (default), otherwise the returned array will be forced to be a base-class array.

copybool, optional
By default, astype always returns a newly allocated array. If this is set to false, and the dtype, order, and subok requirements are satisfied, the input array is returned instead of a copy.

Returns
arr_tndarray
Unless copy is False and the other conditions for returning the input array are satisfied (see description for copy input parameter), arr_t is a new array of the same shape as the input array, with dtype, order given by dtype, order.

Raises
ComplexWarning
When casting from complex to float or int. To avoid this, one should use a.real.astype(t).
'''
import numpy as np

x = np.array([1, 2, 2.5])
print(x.dtype)

x_new = x.astype(np.int8)
print(x_new.dtype)
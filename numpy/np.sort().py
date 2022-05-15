'https://numpy.org/doc/stable/reference/generated/numpy.sort.html'

'''
numpy.sort(a, axis=- 1, kind=None, order=None)[source]
Return a sorted copy of an array.

Parameters
aarray_like
Array to be sorted.

axisint or None, optional
Axis along which to sort. If None, the array is flattened before sorting. The default is -1, which sorts along the last axis.

kind{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional
Sorting algorithm. The default is ‘quicksort’. Note that both ‘stable’ and ‘mergesort’ use timsort or radix sort under the covers and, in general, the actual implementation will vary with data type. The ‘mergesort’ option is retained for backwards compatibility.

Changed in version 1.15.0.: The ‘stable’ option was added.

orderstr or list of str, optional
When a is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string, and not all fields need be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

Returns
sorted_arrayndarray
Array of the same type and shape as a.
'''

import numpy as np

a = np.array([[1,4],[3,1]])
print(a)

print(np.sort(a)) # sort along the last axis (axis = 1 -> horizontally -> sort every row)

print(np.sort(a, axis=None)) # sort the flattened array

print(np.sort(a, axis=0)) # sort along the first axis (axis = 0 -> vertically -> sort every column)


# Use the 'order' keyword to specify a field to use when sorting a structured array:
dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype) # create a structured array
print(a)
print(np.sort(a, order='height'))

# Sort by age, then height, if ages are equal:
print(np.sort(a, order=['age', 'height']))
'''
https://appdividend.com/2021/07/05/how-to-flatten-list-in-python/

Transforming a list of lists into a list is called “flattening a list“.
'''

# Method 1: Using List Comprehension
original_list = [[11, 21, 30], [19, 63, 71], [81, 99]]
flatten_list = [element for sublist in original_list for element in sublist]

print("Original list", original_list)
print("Flattened list", flatten_list)


# Method 2: Using itertools
# It treats consecutive sequences as a single sequence by iterating through the iterable passed as the argument sequentially.
from itertools import chain

original_list = [[11, 21, 30], [19, 63, 71], [81, 99]]
flatten_list = list(chain(*original_list))

print("Original list", original_list)
print("Flattened list", flatten_list)


# Method 3: Using numpy (concatenate() and flat())
import numpy as np

original_list = [[11, 21, 30], [19, 63, 71], [81, 99]]
flatten_list = list(np.concatenate(original_list).flat)

print(np.concatenate(original_list))

print("Original list", original_list)
print("Flattened list", flatten_list)

# Method 4
lst = [0, 2, (1, 2), 5, 2, (3, 5)]
#lst = [1, 2, 3]
lst_flat = [y for x in lst for y in (x if isinstance(x, tuple) else (x,))]
print(lst_flat)


# Method 5
from pandas.core.common import flatten

my_list = [0, 1, [2, 3, [4, 5]]]
print(list(flatten(my_list)))
# [0, 1, 2, 3, 4, 5]

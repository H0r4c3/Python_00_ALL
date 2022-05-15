'''
Split an array into smaller arrays over the first rows
For example:
[[0 1 2]
[3 4 5]
[6 7 8]]

splitted into:

[[0 1]
[3 4]]
and
[[1 2]
[4 5]]
'''

import numpy as np

def split_1D_array(my_array, new_length):
    list_of_1D_arrays = list()
    for i in range(len(my_array)-1):
        list_of_1D_arrays.append(my_array[i : i + new_length])
    
    return list_of_1D_arrays


def split_2D_array(my_array, rows, columns):
    list_of_arrays = list()
    arr = [None]*2
    
    # row 0
    arr0 = split_1D_array(my_array[0], columns)
    
    # row 1
    arr1 = split_1D_array(my_array[1], columns)
    
    return list(zip(arr0, arr1))

my_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
my_array = np.array(my_list)
print(my_array)

list_of_arrays = split_2D_array(my_list, 2, 2)
print(list_of_arrays)
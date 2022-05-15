import numpy as np
def split_1D_array(my_arr, new_length):
    list_of_arrays = list()
    for i in range(len(my_arr)):
        list_of_arrays.append(my_arr[i : i + new_length])
    
    return list_of_arrays

my_list = [0, 1, 2, 3, 4, 5, 6]
my_arr = np.array(my_list)
list_of_arrays = split_1D_array(my_arr, 2)

print(my_list)
print(list_of_arrays)
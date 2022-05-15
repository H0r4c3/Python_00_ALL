
import numpy as np

my_list = [[1, 2], [1, 2, 3], [1]]

# find the length of the longest list
length = max(map(len, my_list))

# make the lists equal in length
my_list_equal_len = [item + [None]*(length-len(item)) for item in my_list]

my_arr = np.array(my_list_equal_len)

print(my_arr)
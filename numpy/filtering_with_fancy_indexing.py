'https://campus.datacamp.com/courses/introduction-to-numpy/selecting-and-updating-data?ex=5'

import numpy as np
my_arr = np.array([1, 2, 3, 4, 5, 6])

# create a mask for even numbers
mask = my_arr % 2 == 0

# filter the array using mask
print(my_arr[mask])
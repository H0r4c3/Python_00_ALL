import numpy as np

my_string = '12345'

my_arr = np.fromstring(my_string, dtype=int, sep=' ')

print(my_arr)
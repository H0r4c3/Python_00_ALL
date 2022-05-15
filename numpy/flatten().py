
import numpy as np

np_arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(np_arr)

np_arr2 = np.reshape(np_arr, (2, 4))
print(np_arr2)

np_arr3 = np.transpose(np_arr2)
print(np_arr3)

np_arr4 = np_arr3.flatten()
print(np_arr4)
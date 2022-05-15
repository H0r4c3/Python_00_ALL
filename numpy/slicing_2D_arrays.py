import numpy as np

arr_old = np.array([[0,1,2,3,4],
                [5,6,7,8,9],
                [10,11,12,13,14],
                [15,16,17,18,19],
                [20,21,22,23,24]])

print(arr_old)

# Slicing on rows and columns
arr_new = arr_old[1:4, 1:4]
print(arr_new)

# Print the first row
print(arr_old[0])

# Print the first column
print(arr_old[ : , 0])


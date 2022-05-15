'https://www.datacamp.com/community/tutorials/python-numpy-tutorial'

# Import `numpy` as `np`
import numpy as np

# Make the array `my_array`
my_array = np.array([[1,2,3,4,5], [5,6,7,8,9]], dtype=np.int64)

# Print `my_array`
print("\n my_array: \n", my_array)

# Print the number of `my_array`'s dimensions
print("\n ndim: \n", my_array.ndim)

# Print the number of `my_array`'s elements
print("\n size: \n", my_array.size)

# Create a 1-d array
x = np.arange(10)
print("\n a 1-d array: \n", x)

# Select the element at the 1st and 4th indexes
print("\n x[[1, 4]] = element at the 1st and 4th indexes: \n", x[[1, 4]])

# Create a 2-d array from a 1-d array using 'shape'
x.shape = (2,5)
print("\n a 2-d array shaped from a 1-d array: \n", x)


# Select items at index 0 and 1
print("\n my_array[0:2]: \n", my_array[0:2])

# Select items at row 0 and 1, column 1
print("\n my_array[0:2,1]: \n", my_array[0:2,1])

# Select the element at the 1st index from a 2-d array
print("\n my_array[1] = element at the 1st index: \n", my_array[1])

# Select the element at row 1 column 2
print("\n my_array[1][2] = element at row 1 column 2: \n", my_array[1][2])

# Select the element at row 1 column 2
print("\n my_array[1,2] = element at row 1 column 2: \n", my_array[1,2])

# Select the min
print("\n min: \n", my_array.min())

# Create an array of ones
print("\n ones: \n", np.ones((3,4)))

# Create an array of zeros
print("\n zeros: \n", np.zeros((2,3,4),dtype=np.int16))

# Create an array with random values
print("\n random: \n", np.random.random((2,2)))

# Create an empty array
print("\n empty: \n", np.empty((3,2)))

# Create a full array
print("\n full: \n", np.full((2,2),7))

# Create an array of evenly-spaced values
print("\n arange: \n", np.arange(10,25,5))

# Create an array of evenly-spaced values
print("\n linspace: \n", np.linspace(0,2,9))


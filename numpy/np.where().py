'https://thispointer.com/numpy-where-tutorial-examples-python/'

'''
numpy.where(condition[, x, y])

condition: A conditional expression that returns a Numpy array of bool

x, y: Arrays (Optional i.e. either both are passed or not passed)
If x & y are passed in np.where(), then it returns the elements selected from x & y based on condition on original array depending 
on values in bool array yielded by the condition.

Returns: INDEXES!!!

If x & y parameters are passed then it returns a new numpy array by selecting items from x & y based on the result from applying condition on original numpy array.
If x & y arguments are not passed and only condition argument is passed then it returns the indices of the elements that are True in bool numpy array. 
If the original array is multidimensional, then it returns a tuple of arrays (one for each axis).
'''

import numpy as np

# 1. Example

# Create a numpy array from list
arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])

# Get the indexes of elements based on conditions
result = np.where((arr > 12) & (arr < 16))
print(result)


# 2. Example

# Create a numpy array from a list of numbers
arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])

# Get the index of elements with value 15
result = np.where(arr == 15)
print(result)


# 3. Example
an_array = np.array([3, 23,  5, 67, 12, 15, 89])
an_array = np.where(an_array > 20, 0, an_array) # replace the items > 20 with value 0
print(an_array)


# 4. Example
cryptogram = "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz"
crypto = list(cryptogram)
crypto_arr = np.array(crypto).reshape(8, 8)
print(crypto_arr)

result = np.where((crypto_arr == 'q') | (crypto_arr == 'u') | (crypto_arr == 'i') | (crypto_arr == 'c'), 'X', '.')
print(result)
    
x, y = np.where((crypto_arr == 'q') | (crypto_arr == 'u') | (crypto_arr == 'i') | (crypto_arr == 'c'))
print(list(zip(x, y)))


# 5. Example: replace the values which does not fulfill the condition, with 'NOK', the rest does not change

a = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])

b = np.where(a < 4, a, 'NOK')  # 'NOK' is broadcast (does not fulfill the condition; these values are replaced by 'NOK')
print(b)
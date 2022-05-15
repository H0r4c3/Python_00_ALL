'https://appdividend.com/2022/02/17/np-argmin/'

'''
The np.argmin() function is used to get the indices of the minimum element from an array (single-dimensional array) or 
any row or column (multidimensional array) of any given array. 
The numpy argmin() function takes arr, axis, and out as parameters and returns the array.

numpy.argmin(arr,axis=None,out=None)

The numpy argmin() function takes three arguments:

arr: The array from which we want the indices of the min element.
axis: By default, it is None. But for the multidimensional array, if we’re going to find an index of any maximum of element row-wise or column-wise, we have to give axis=1 or axis=0, respectively.
out: If provided, the result will be inserted into this array. It should be of the appropriate shape and dtype.

The np.argmin() function returns an array containing the indices of the minimum elements.
'''

#Importing numpy
import numpy as np

#We will create an 1D array
arr = np.array([42, 13, 24, 63, 121, 13, 64])
#Printing the array
print("The array is: ", arr)
#Shape of the array
print("Shape of the array is : ", np.shape(arr))

#Now we will print index of min value of this array
print("Index of minimum value of the given array is: ", np.argmin(arr))




# Finding indices of maximum elements from Multidimensional Array

arr = np.array([(1, 9, 4), (6, 55, 4), (1, 3, 40), (5, 6, 4)])

print("The array is: ")
print(arr)

#Indices of minimum value of each row
a = np.argmin(arr, axis=1)
print("Indices of minimum value of each row of the array is: ", a)

#Indices of minimum value of each column
b = np.argmin(arr, axis=0)
print("Indices of minimum value of each column of the array is: ", b)
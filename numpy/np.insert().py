'https://appdividend.com/2022/02/24/np-insert/'

'''
The np.insert() is a numpy library function that inserts values in the input array along the given axis and before a given index. 
If a value type is converted to be inserted, it is different from an input array. 
Insertion is not in place, and the method returns the new array. Also, an input array is flattened if the axis is not mentioned.

numpy.insert(array, object, values, axis = None)

The numpy.insert() function takes four parameters:

array -> is the name of the array in which the value to be inserted
object -> This can be an integer or a list of an array (subarray) before which the given value is to be inserted.
values -> This is the value that is to be inserted in the array. If the type of value is not the same as the array type, then the value is converted into that type.
axis -> This is applicable for multidimensional arrays. By default, the value of the axis is None. 
But, the multidimensional array helps us insert the value in a particular axis.

The insert() method returns a copy of the array with the value inserted as per the mentioned object in a particular axis.
'''

import numpy as np

arr1 = np.arange(10, 16)
print("The array is: ", arr1)

# Now we will insert a value before the value 12
obj = 2
value = 40

# Inserting value
arr = np.insert(arr1, obj, value, axis=None)

print("After inserting, the new array is: ")
print(arr)



# Insert in Multidimensional Array
arr2 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (50, 51, 52)])
print("The array is: ")
print(arr2)

# This will insert two new rows with value
# 50 and 100 respectively before the row 1
a = np.insert(arr2, 1, [[50], [100], ], axis=0)

# printing new array
print("New array is : ")
print(a)
'https://www.geeksforgeeks.org/python-set-issubset-method/'

'''
Python set issubset() method returns True if all elements of a set A are present in another set B which is passed as an argument, 
and returns False if all elements are not present in Python.

Python Set issubset() Method Syntax:
Syntax: set_obj.issubset(other_set)

Parameter:

other_set: any other set to compare with.

Return: bool
'''

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}

# Output True, since s2 elements in s1
print(s2.issubset(s1))
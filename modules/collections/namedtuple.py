'https://www.geeksforgeeks.org/namedtuple-in-python/'

'''
Named tuples allow you to create tuples and assign meaningful names to the positions of the tuple’s elements.

The namedtuple function accepts the following arguments to generate a class:
A class name that specifies the name of the named tuple class.
A sequence of field names that correspond to the elements of tuples. The field names must be valid variable names except that they 
cannot start with an underscore (_).

Python supports a type of container like dictionaries called “namedtuple()” present in module, “collections“. 
Like dictionaries, they contain keys that are hashed to a particular value. 
But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.
'''


from collections import namedtuple

# Declaring namedtuple()  
Student = namedtuple('Student', ['name', 'age', 'DOB'])  
      
# Adding values  
S = Student('Nandini', '19', '2541997')  
print(S)
      
# Access using index  
print (f"The Student age using index is : {S[1]}")  
      
# Access using name   
print (f"The Student name using keyname is : {S.name}")
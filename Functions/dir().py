'https://www.programiz.com/python-programming/methods/built-in/dir'

'''
The dir() method tries to return a list of valid attributes of the object.

dir() Parameters:
dir() takes maximum of one object.

object (optional) - dir() attempts to return all attributes of this object.

Return Value from dir():
dir() tries to return a list of valid attributes of the object.

If the object has __dir__() method, the method will be called and must return the list of attributes.
If the object doesn't have __dir__() method, this method tries to find information from the __dict__ attribute (if defined), and from type object. In this case, the list returned from dir() may not be complete.
If an object is not passed to dir() method, it returns the list of names in the current local scope.
'''

number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())

print('\n dir(str) \n')
print(dir(str))
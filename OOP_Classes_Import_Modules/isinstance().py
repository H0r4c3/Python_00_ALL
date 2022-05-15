'https://www.w3schools.com/python/ref_func_isinstance.asp'

'''
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

Synthax:
isinstance(object, type)

object	Required. An object.
type	A type or a class, or a tuple of types and/or classes
'''

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
print(x)


x = isinstance(5, int)
print(x)

x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)
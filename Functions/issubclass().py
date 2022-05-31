'https://www.programiz.com/python-programming/methods/built-in/issubclass'

'''
The issubclass() function checks if the class argument (first argument) is a subclass of classinfo class (second argument).

The syntax of issubclass() is:

issubclass(class, classinfo)

issubclass() takes two parameters:

class - class to be checked
classinfo - class, type, or tuple of classes and types


issubclass() returns:
True if class is subclass of a class, or any element of the tuple
False otherwise
'''

class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
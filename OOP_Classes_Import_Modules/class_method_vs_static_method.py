'https://www.geeksforgeeks.org/class-method-vs-static-method-python/'

'''
A class method is a method that is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.

A static method is also a method that is bound to the class and not the object of the class.
A static method can’t access or modify the class state.
It is present in a class because it makes sense for the method to be present in class.

Class method vs Static Method
A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. 
On the other hand, class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
When to use what?
We generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''


#Python program to demonstrate use of class method and static method.

from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
      
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
  
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
  
print (person1.age)
print (person2.age)
  
# print the result
print (Person.isAdult(22))
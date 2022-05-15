# https://www.programiz.com/python-programming/methods/built-in/property

'''
The property() construct returns the property attribute.
property() returns the property attribute from the given getter, setter, and deleter.
'''

# Example 1: Create attribute with getter, setter, and deleter


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name

'''
Here, _name is used as the private variable for storing the name of Person.
We also set:
a getter method get_name() to get the name of the person,
a setter method set_name() to set the name of the person,
a deleter method del_name() to delete the name of the person.
Now, we set a new property attribute name by calling the property() method.
As shown in the program, referencing p.name internally calls get_name() as getter, set_name() as setter and del_name() as deleter through the printed output present inside the methods.
'''

# Example 2: Using @property decorator


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name

'''
Instead of using property(), you can use the Python decorator @property to assign the getter, setter, and deleter.
First, we specify that name() method is also an attribute of Person. This is done by using @property before the getter method as shown in the program.
Next, we use the attribute name to specify the setter and the deleter.
This is done by using @name.setter for the setter method and @name.deleter for the deleter method.
Notice, we've used the same method name() with different definitions for defining the getter, setter, and deleter.
Now, whenever we use p.name, it internally calls the appropriate getter, setter, and deleter as shown by the printed output present inside the method.
'''

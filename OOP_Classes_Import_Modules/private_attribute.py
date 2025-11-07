class MyClass:
    def __init__(self):
        # Strongly private attribute
        self.__my_private_attribute = 42

    def get_private_attribute(self):
        return self.__my_private_attribute

# Create an instance of the class
obj = MyClass()

# Access the private attribute using a method
value = obj.get_private_attribute()
print("Value of private attribute:", value)

# Access the private attribute directly (not recommended)
direct_access = obj._MyClass__my_private_attribute
print("Direct access to private attribute:", direct_access)


'''
In the above example, __my_private_attribute is a private attribute, and its name is mangled to _MyClass__my_private_attribute. 
Although it's technically possible to access the private attribute directly using the mangled name, 
it's not recommended, as it goes against the principle of encapsulation.

It's important to respect encapsulation and not access private attributes from outside the class unless absolutely necessary. 
If you need to provide access to certain attributes, consider creating getter and setter methods to control access and modifications.
'''
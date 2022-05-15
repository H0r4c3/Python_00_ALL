# https://www.programiz.com/python-programming/object-oriented-programming
# https://www.programiz.com/python-programming/class


# Example1:

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Blu is a {}".format(Parrot.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))



'''
In the above program, we created a class with the name Parrot. Then, we define attributes. The attributes are a characteristic of an object.
These attributes are defined inside the __init__ method of the class. It is the initializer method that is first run as soon as the object is created.
Then, we create instances of the Parrot class. Here, blu and woo are references (value) to our new objects.
We can access the class attribute using __class__.species. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using blu.name and blu.age. 
However, instance attributes are different for every instance of a class.
'''


# Example 2:

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: 10
p = Person()
print(p.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: 'This is a person class'
print(Person.__doc__)

'''
As soon as we define a class, a new class object is created with the same name. This class object allows us to access the different attributes as well as to instantiate new objects of that class.
'''


# Example 3:

class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
####print(num1.attr)

'''
In the above example, we defined a new class to represent complex numbers. 
It has two functions, __init__() to initialize the variables (defaults to zero) and get_data() to display the number properly.
An interesting thing to note in the above step is that attributes of an object can be created on the fly. We created a new attribute attr for object num2 and read it as well. 
But this does not create that attribute for object num1.
'''


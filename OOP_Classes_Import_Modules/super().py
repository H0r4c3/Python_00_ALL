'https://www.geeksforgeeks.org/python-super/'

'''
In Python, the super() function is used to refer to the parent class or superclass. 
It allows you to call methods defined in the superclass from the subclass, enabling you to extend and 
customize the functionality inherited from the parent class.

In the given example, The Emp class has an __init__ method that initializes the id, and name and address attributes. 
The Freelance class inherits from the Emp class and adds an additional attribute called email. 
It calls the parent class’s __init__ method super() to initialize the inherited attribute.

Benefits of Super Function:
Need not remember or specify the parent class name to access its methods. This function can be used both in single and multiple inheritances.
This implements modularity (isolating changes) and code reusability as there is no need to rewrite the entire function.
The super function in Python is called dynamically because Python is a dynamic language, unlike other languages.

Understanding Python super() with __init__() methods
Python has a reserved method called “__init__.” In Object-Oriented Programming, it is referred to as a constructor. 
When this method is called it allows the class to initialize the attributes of the class. In an inherited subclass, a parent class can 
be referred to with the use of the super() function. 
The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.
'''

class Emp():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
 
# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, address, email):
        super().__init__(id, name, address)
        self.email = email
 
Emp_1 = Freelance(103, "Name_1", "Address_1" , "email_1@gmail.ro")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.address)
print('The Emails is:', Emp_1.email)
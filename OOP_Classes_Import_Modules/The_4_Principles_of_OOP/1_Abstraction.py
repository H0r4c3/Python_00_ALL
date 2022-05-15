'https://info.keylimeinteractive.com/the-four-pillars-of-object-oriented-programming'

'''
Abstraction is an extension of encapsulation. It is the process of selecting data from a larger pool to show only the relevant details to the object.

Basically, Abstraction focuses on hiding the internal implementations of a process or method from the user. 
In this way, the user knows what he is doing but not how the work is being done.

For example, people do not think of a car as a set of thousands of individual parts. 
Instead they see it as a well-defined object with its own unique behavior. 
This abstraction allows people to use a car to drive without knowing the complexity of the parts that form the car. 
They can ignore the details of how the engine transmission, and braking systems work. 
Instead, they are free to utilize the object as a whole.
'''


'''
Here, abs_class is the abstract class inside which abstract methods or any other sort of methods can be defined.

As a property, abstract classes can have any number of abstract methods coexisting with any number of other methods. For example we can see below.

Here, method() is normal method whereas Abs_method() is an abstract method implementing @abstractmethod from the abc module.
'''

from abc import ABC, abstractmethod
class abs_class(ABC):
    
    #normal method
    def method(self):
        #method definition
        pass
    
    @abstractmethod
    def Abs_method(self):
        #Abs_method definition
        pass
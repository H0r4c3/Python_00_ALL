'''
When we create a Car instance, several things happen:

The Car's __init__ method runs
Inside __init__, we create a new Engine instance with Engine()
We store that Engine instance in the attribute self.engine
Now the Car instance has an Engine instance as part of its state

This works because in Python, attributes can store any type of data:

Simple types like numbers: self.speed = 0
Strings: self.color = "red"
Lists: self.passengers = []
And yes, even instances of other classes: self.engine = Engine()
'''

from Engine_file import Engine

class Car:
    def __init__(self):
        # Here's where we create an Engine instance as an attribute
        self.engine = Engine()
    
    def start_car(self):
        # Now we can use the engine instance's methods
        return self.engine.start()

# Create a car
my_car = Car()
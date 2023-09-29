'https://python.plainenglish.io/mastering-python-the-10-most-difficult-concepts-and-how-to-learn-them-3973dd15ced4'

# 1. Object-oriented programming (OOP)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")

my_dog = Dog("Fido", "Golden Retriever")
print(my_dog.name) # "Fido"
my_dog.bark() # "Woof!"


# 2. Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()


# 3. Generator expressions and yield

# generator function
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# using for loop
for item in my_gen():
    print(item)
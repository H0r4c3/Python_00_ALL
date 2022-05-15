'https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/'

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        
my_python = Snake('Python')
print(my_python.name)

my_python.name = 'XXX'
print(my_python.name)

my_python.change_name('New Name')
print(my_python.name)
'https://medium.com/pythoneers/best-practices-to-follow-while-creating-classes-in-python-4497bc8535dc'
'https://www.machinelearningplus.com/python/object-oriented-programming-oops-in-python/'

'''
__str__ : Controls how the class instance is printed
__repr__: Controls how the class instance is shown in interpreter
'''

class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return f'{self.name} {self.surname}'
    

my_object = Student('Horatiu', 'Crista')

print(my_object)

print(my_object.name, my_object.surname)
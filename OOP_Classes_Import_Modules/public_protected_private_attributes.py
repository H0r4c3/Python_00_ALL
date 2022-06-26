'https://www.tutorialsteacher.com/python/public-private-protected-modifiers'

# PRIVATE

class Person:
    __class_att = 'private class attribute' # private class attribute
    
    def __init__(self, name, age):
        self.__name = name # private instance attribute
        self.__age = age # private instance attribute
        
    def __display(self):  # private method
	    print('This is private method!!!')
     

person1 = Person('John', 20)

#print(person1.__class_att)
#print(person1.__name)
#print(person1.__age)
#person1.__display()

# Here, we do not access the private instance attribute "__name", but we create a new attribute named "__name" ONLY for the object person1 !!!
person1.__name = 'New'
print(person1.__name)

person1.x = 'X'
print(person1.x)

# Error, because the attribute "__name" was created ONLY for the object person1 !!!
person2 = Person('J', 25)
#print(person2.__name)


'''
Python doesn't have private attributes. 
Python doesn't have any access modifiers. What you are using here is double-underscore name-mangling. That is not the same as private. 
It simply mangles the name to _MyClass__my_attribute to prevent accidental name-collisions in subclasses, it is still completely accessible from the outside.
'''

# We can access the private attribute, too!!!
print(person1._Person__name)

# And the private method, too!!!
person1._Person__display()

'''
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. 
This concept is called Polymorphism.
'''



'''
In the next program, we defined two classes Parrot and Penguin. Each of them have a common fly() method. However, their functions are different.
To use polymorphism, we created a common interface i.e flying_test() function that takes any object and calls the object's fly() method. 
Thus, when we passed the blu and peggy objects in the flying_test() function, it ran effectively.
'''

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


'''
Next, follows an example demonstrating method overriding in action:
'''

class ClassA:
    def my_lovely_method(self):
        print("my_lovely_method() method from class A")


class ClassB(ClassA):
    def my_lovely_method(self):
        print("my_lovely_method() method from class B")


object_a = ClassA()
object_b = ClassB()
object_a.my_lovely_method()
object_b.my_lovely_method()

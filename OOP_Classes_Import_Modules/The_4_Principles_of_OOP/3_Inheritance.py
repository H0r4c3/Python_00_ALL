'''
Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). 
Similarly, the existing class is a base class (or parent class).
'''

# Example1:

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


'''
In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the swim() method.
Again, the child class modified the behavior of the parent class. We can see this from the whoisThis() method. 
Furthermore, we extend the functions of the parent class, by creating a new run() method.
Additionally, we use the super() function inside the __init__() method. This allows us to run the __init__() method of the parent class inside the child class.
'''


# Example2:

'''This class has data attributes to store the number of sides n and magnitude of each side as a list called sides.'''

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


'''
A triangle is a polygon with 3 sides. So, we can create a class called Triangle which inherits from Polygon. This makes all the attributes of Polygon class available to the Triangle class.
We don't need to define them again (code reusability). Triangle can be defined as follows.
However, class Triangle has a new method findArea() to find and print the area of the triangle.
'''

class Triangle(Polygon):
    def __init__(self):
        #Polygon.__init__(self, 3)
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

'''
In the above example, notice that __init__() method was defined in both classes, Triangle as well Polygon. When this happens, the method in the derived class overrides that in the base class. 
This is to say, __init__() in Triangle gets preference over the __init__ in Polygon.
Generally when overriding a base method, we tend to extend the definition rather than simply replace it. 
The same is being done by calling the method in base class from the one in derived class (calling Polygon.__init__() from __init__() in Triangle).
A better option would be to use the built-in function super(). So, super().__init__(3) is equivalent to Polygon.__init__(self,3) and is preferred. 
'''

# Example3: Multiple Inheritance

'''
The MultiDerived class inherits from both Base1 and Base2 classes.
Every class in Python is derived from the object class. It is the most base type in Python.
'''

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
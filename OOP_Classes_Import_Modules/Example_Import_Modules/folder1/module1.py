import sys

#sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\0_ALL\OOP_Classes_Modules\Example_Modules')

from folder2.module2 import Account2

class Account1:
    def __init__(self, username1, password1):
        self.username1 = username1
        self.password1 = password1

    def method1(self):
        print('username1: ', self.username1)
        print('password1: ', self.password1)

employee1 = Account1('u1', 'pw1')
employee2 = Account2('u2', 'pw2')

employee1.method1()
employee2.method2()


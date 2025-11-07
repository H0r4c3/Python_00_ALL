'https://www.geeksforgeeks.org/args-kwargs-python/'

'''
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
It is used to pass a non-key worded, variable-length argument list.
'''

#Example nr. 1
def my_function(*args):
    for arg in args:
        print (arg)
        
my_function(1, 2, 3, 4)

my_function(4, 3, 3, 1, 7, 5, 3, 3, 3, 2)

#Example nr. 2
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)


'''
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
'''

def myFun(**kwargs):
    for key, value in kwargs.items():
        print (key, value)
        
myFun(first ='Geeks', mid ='for', last='Geeks')
'''
A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way.

new_function = decorator_function(old_function)
'''

# BEST example (with order of execution!!!)
# Explanation: The numbers mean the execution order
print('\n1. Example:\n')

def my_decorator(my_old_func): # 3
    
    def wrapper(): # 4
        print('new_function is called') 
        my_old_func() # 5
        
        
    print('my_decorator have started') # 3
    
    return wrapper
    
@my_decorator # 2
def old_function(): # 6
    print('old_function is called')
    

old_function() # 1



# Another very clear EXAMPLE:
# https://www.bogotobogo.com/python/python_decorators.php
'''
A decorator gives an existing function a new behavior, without changing the function itself.

'''
print('\n2. Example:\n')

def myDecorator(myfunc):
    
    def wrapper(n):
        return '$' + myfunc(n)
           
    return wrapper

@myDecorator
def myFunction(a):
    return(a)

# call the decorated function
print(myFunction('100'))




# Another example: A decorator for rounding the result

print('\n3. Example:\n')

# This Decorator is rounding the result of my_function() to the 2 decimal points
def rounded(my_func): 
    return lambda x: round(my_func(x), 2)

'''
def rounded(my_func): 
    def wrapper(x):
        return round(my_func(x), 2)
    return wrapper
'''

@rounded
def my_function(n):
    return n/3

# call the decorated function
print(my_function(4))


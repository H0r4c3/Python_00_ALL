'https://www.udemy.com/course/python-programming-beginner-to-advanced/learn/lecture/17944186#overview'
'https://www.csestack.org/python-decorators/'

'''
A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way.

new_function = decorator(old_function)
'''

# 1. The example from the course:
print('\n1. Example from course:\n')

def deco(func):
    def new_func(val1, val2):
        if type(val1)==type(val2):
            return func(val1, val2)
        else:
            return func(str(val1), str(val2))
    return new_func

@deco
def concat(val1, val2):
    return val1 + val2

result = concat(10, 10)
print(result)

result = concat('string1', 'string2')
print(result)

result = concat(20, 'string3')
print(result)


# 2. My Example:
# BEST BEST BEST (with order of execution!!!)
# Explanation: The numbers mean the execution order
print('\n2. My Example:\n')

def my_decorator(func): # 3
    
    def new_function(): # 4
        print('new_function is called') 
        func() # 5
        
    print('my_decorator have started') # 3
    
    return new_function
    
@my_decorator # 2
def old_function(): # 6
    print('old_function is called')
    

old_function() # 1


# 3. Decorator with arguments:

def smart_divide(func):
    def inner(a, b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            print("Cannot divide by 0 !!!")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(20, 5)
divide(20, 0)


# 4. Chain of Decorators
def bold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped

def italic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@bold
@italic
def hello():
    return 'hello'

print(hello()) # -> <b><i>hello</i></b>
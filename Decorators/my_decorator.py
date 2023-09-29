'''
Decorator - explanations

The order of execution is:
1. @my_decorator
2. my_decorator(func) -> print 1. -> print 2. -> return wrapper
3. wrapper() -> print 3. -> func() -> my_function() -> print 4. -> print 5.
'''

def my_decorator(func):
    print('1. my_decorator has started.')
    
    def wrapper():
        print('3. Before the function my_function is called.')
        func()
        print('5. After the function my_function is called.')
    
    print('2. my_decorator continues.')
        
    return wrapper

@my_decorator
def my_function():
    print('4. The function my_function is called!')



my_function()

'''
This is equivalent to calling my_function and passing it as an argument to my_decorator, like this:

my_function = my_decorator(my_function)
'''

def my_decorator(func):
    '''Decorator function'''
    def wrapper(): 
        # Do something before
        result = 'MY_DECORATOR'
        # Do something after
        return result
    return wrapper

@my_decorator
def my_function():
    result = 'my_function'
    return result

print(my_function())
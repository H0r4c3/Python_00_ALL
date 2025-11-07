'''
In Python, using functools.wraps in decorators serves to preserve the metadata of the original function being decorated. 
Without functools.wraps, the decorated function's metadata (like its name, docstring, and other attributes) 
would be replaced by those of the wrapper function, which can cause confusion and make debugging or introspection more difficult.

Here's what functools.wraps does:
functools.wraps is a decorator provided by the functools module. 
It is applied to the wrapper function inside a custom decorator and takes the original function as its argument. 
When used, it updates the wrapper function's attributes to match those of the original function.

Conclusion:
Using functools.wraps is a best practice when writing decorators in Python. 
It ensures that the decorated function retains its original metadata, making the code easier to understand, debug, and maintain.
'''

import functools

#1. Without functools.wraps:

# Without functools.wraps
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@my_decorator
def my_function():
    """Original docstring"""
    print("Hello, world!")

print(my_function.__name__)  # Output: wrapper
print(my_function.__doc__)   # Output: Wrapper docstring


#2. With functools.wraps:

# With functools.wraps
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@my_decorator
def my_function():
    """Original docstring"""
    print("Hello, world!")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: Original docstring

# 0. https://realpython.com/primer-on-python-decorators/

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# 1. https://realpython.com/primer-on-python-decorators/

import functools

def do_twice(func):
    @functools.wraps(func) # decorator to preserve the name and docstring of the original function
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello, {name}!")

greet('Horace')


# 2. Decorator with arguments

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Run {name}")

greet('Multiple Times')
    
    
# 2. Timing function: It will measure the time a function takes to execute and print the duration to the console

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)])
        
# for testing the timer decorator        
waste_some_time(1000)


# 3. Another Timing function: It will measure the time a function takes to execute and print the duration to the console
import time

def timer2(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        # return the result of the decorated function execution
        return result
    # return reference to the wrapper function
    return wrapper


# 4. https://medium.com/@ayush-thakur02/python-decorators-that-can-reduce-your-code-by-half-b19f673bc7d8

from functools import wraps

def memoize(func):
    '''
    This decorator is useful for optimizing the performance of recursive or expensive functions, 
    as it caches the results of previous calls and returns them if the same arguments are passed again.
    '''
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@memoize
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(factorial(10))
print(fibonacci(10))



if __name__ == '__main__':
    main()
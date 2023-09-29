'https://medium.com/@angusyuen/writing-maintainable-pythonic-code-metaprogramming-with-decorators-2fc2f1d358db'

'''
Python Decorators are an annotation you place above a function, which allows you to “monkey patch” that function. 
This adds additional functionality that the function did not previously have.
'''

# Create a Python Decorator to centralise the timing logic and reduce the amount of repetition across your codebase.

# All our timing logic is now centralised in this decorator
# So, if we want to make changes to this logic, we just need to modify this function

import math
from timeit import default_timer as timer

def monitor_elapsed_time(my_func):
  
  def wrapper(*args, **kwargs):
    start = timer()
    my_func_result = my_func(*args, **kwargs)
    print(f"Time elapsed: {timer() - start}")
    return my_func_result
    
  return wrapper


@monitor_elapsed_time
def my_function(n):
    result = math.factorial(n)
    return result

print(f'result = {my_function(10)}')
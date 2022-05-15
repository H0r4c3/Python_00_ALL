'https://towardsdatascience.com/the-unknown-features-of-pythons-operator-module-1ad9075d9536'
'https://docs.python.org/3/library/operator.html#mapping-operators-to-functions'

'''
First reason why you might want to use some of these in your code is if you need to pass operator to a function:

def apply(op, x, y):
    return op(x, y)

from operator import mul
apply(mul, 3, 7) # -> 21

Reason why we need to do this is, is that Python’s operators (+, -, …) are not functions, so you cannot pass them directly to functions. 
Instead, you can pass in the version from operator module.

You might also think, I don’t need operator module for this, I can just use lambda expression!.
Functions in this module are faster than lambdas!!!

'''
# 1. Example

from operator import mul

def my_function(op, x, y):
    return op(x, y)

result = my_function(mul, 3, 7) # -> 21
print(result)


# 2. Example
import timeit
from operator import add

lambda_time = timeit.timeit("(lambda x,y: x + y)(12, 15)", number = 1_000_000, globals = globals())
print(f'lambda repeated 1_000_000 times = {lambda_time} seconds')

operator_add_time = timeit.timeit("add(12, 15)", number = 1_000_000, globals = globals())
print(f'operator.add repeated 1_000_000 times = {operator_add_time} seconds')


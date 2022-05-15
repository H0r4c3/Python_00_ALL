'https://www.blog.pythonlibrary.org/2016/02/11/python-partials/'

'''
Python comes with a fun module called functools. One of its classes is the partial class. 
You can use it create a new function with partial application of the arguments and keywords that you pass to it. 
You can use partial to "freeze" a portion of your function's arguments and/or keywords which results in a new object. 
Another way to put it is that partial creates a new function with some defaults. Let's look at an example!
'''

from functools import partial

def add(x, y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))




'''
The partial() is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting 
in a new object with a simplified signature. 
For example, partial() can be used to create a callable that behaves like the int() function where the base argument defaults to two:
'''

from functools import partial

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))
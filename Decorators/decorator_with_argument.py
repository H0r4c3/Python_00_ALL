'https://towardsdatascience.com/an-in-depth-tutorial-to-python-decorators-that-you-can-actually-use-1e34d3d2d305'

'''
Decorators are functions that modify another function. They can change the function’s inputs, its output or even its behavior.
'''

# Let’s start with a very simple decorator:
def add_one(func):
    
    def wrapper(a):
        return func(a + 1)
    return wrapper

# Now, we create a function that squares whatever argument is passed, 
# and we are decorating it with add_one. add_one adds 1 to the argument of the passed function:
@add_one
def square(a):
    return a ** 2

result = square(5)
print(result)
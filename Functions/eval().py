'https://realpython.com/python-eval-function/'

'''
eval() Syntax
The syntax of eval() is:

eval(expression, globals=None, locals=None)
eval() Parameters
The eval() function takes three parameters:

expression - the string parsed and evaluated as a Python expression
globals (optional) - a dictionary
locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

eval() is a built-in- function used in python, eval function parses the expression argument and evaluates it as a python expression. 
In simple words, the eval function evaluates the “String” like a python expression and returns the result as an integer.

eval is not much used due to security reasons. !!!!!!!
Still, it comes in handy in some situations like:
You may want to use it to allow users to enter their own “scriptlets”: small expressions (or even small functions), that can be used to customize the behavior of a complex system.
eval is also sometimes used in applications needing to evaluate math expressions. This is much easier than writing an expression parser.
'''

x = 100
result = eval("x * 2")
print(result)

result = eval("sum([2, 2, 2])")
print(result)
        
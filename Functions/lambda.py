'https://www.programiz.com/python-programming/anonymous-function'

'https://www.w3schools.com/python/python_lambda.asp'

'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.

Syntax:
lambda arguments: expression

name = lambda args: expression      <~~>        def name(args): return expression

Lambda functions can have any number of arguments, but only one expression. The expression is evaluated and returned.
'''

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

mult = lambda x, y : x*y
print(mult(3, 4))



# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)


# Sum of elements of two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple(map(lambda x, y: x + y, tuple1, tuple2))
print(result)
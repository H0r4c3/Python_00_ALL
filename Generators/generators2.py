'https://realpython.com/introduction-to-python-generators/'

'''
When you call a generator function or use a generator expression, you return a special iterator called a generator. 
You can assign this generator to a variable in order to use it. 
When you call special methods on the generator, such as next(), the code within the function is executed up to yield.

When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. 
(In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved.
'''

my_list = [1, 2, 3, 4, 5]

def my_generator():
    for item in my_list:
        yield item

result = my_generator()

print(next(result))
print(next(result))
print(next(result))
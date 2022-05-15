'https://www.machinelearningplus.com/python/what-does-yield-keyword-do/'

'''
What does the yield keyword do?
yield in Python can be used like the return statement in a function. When done so, the function instead of returning the output, 
it returns a generator that can be iterated upon. You can then iterate through the generator to extract items. 
Iterating is done using a for loop or simply using the next() function. But what exactly happens when you use yield? 
What the yield keyword does is as follows: Each time you iterate, Python runs the code until it encounters a yield statement inside the function. 
Then, it sends the yielded value and pauses the function in that state without exiting. 
When the function is invoked the next time, the state at which it was last paused is remembered and execution is continued from that point onwards. 
This continues until the generator is exhausted. What does remembering the state mean? It means, any local variable you may have created inside 
the function before yield was called will be available the next time you invoke the function. This is NOT the way a regular function usually behaves. 
Now, how is it different from using the return keyword? Had you used return in place of yield, the function would have returned the respective value, 
all the local variable values that the function had earlier computed would be cleared off and the next time the function is called, 
the function execution will start fresh. Since the yield enables the function to remember its ‘state’, this function can be used to generate 
values in a logic defined by you. So, it function becomes a ‘generator’.
'''

# Function returns a generator when it encounters 'yield'.
def simple_generator():
    x = 1
    yield x
    yield x + 1
    yield x + 2

generator_object = simple_generator()
print(generator_object)  # only generator. no code runs. no value gets returned

# Now you can iterate through the generator object. But it works only once!!! 
for i in generator_object:
    print(i)
    
# Calling the generator the second time wont give anything. Because the generator object is already exhausted and has to be re-initialized. 
# If you call next() over this iterator, a StopIteration error is raised:
for i in generator_object:
    print(i)
    
#next(generator_object) # -> StopIteration Error


# Another GENERATOR:
# Print squares of numbers from 1 to 10, using GENERATOR
def squares(x=0):
    while x < 10:
        x = x + 1
        yield x*x

for i in squares():
    print(i)
    
    
'''
Generators are memory efficient because the values are not materialized until called.

Can a generator be materialized to a list? Yes. You can do so easily using list comprehensions or by simply calling list().
'''

# Materialize list from generator using list comprehension
materialized_list = [i for i in squares()]

# Materialize list from generator using list()
materialized_list = list(squares())

'''
How yield works, step by step
yield is a keyword that returns from the function without destroying the state of it’s local variables. 
When you replace return with yield in a function, it causes the function to hand back a generator object to its caller. 
In effect, yield will prevent the function from exiting, until the next time next() is called. 
When called, it will start executing from the point where it paused before.
'''

def generator_func():
    num = 1
    print("First time execution of the function")
    yield num
    
    num = 10
    print("Second time execution of the function")
    yield num
    
    num = 100
    print("Third time execution of the function")
    yield num

obj = generator_func()
print(next(obj))
print(next(obj))
print(next(obj))
#print(next(obj))

'''
See that the function printed until the first yield. Now if you iterate again, it will not start from the beginning, it starts from where it left off. 
After exhausting all the yield statements in the function, it will produce a StopIteration error, if called again. 
A generator function can be completely used only once. If you want to iterate through them again, then you need to create the object again.
'''
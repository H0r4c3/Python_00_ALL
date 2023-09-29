'https://chat.openai.com/chat/f1dea883-f7a9-49f3-9153-0d140894d233'

'''
In this example, my_decorator is a decorator function that takes another function func as its argument. 
The decorator function then defines a new function wrapper that will be used to wrap the original function.

The wrapper function contains the code that will be executed before and after the original function func is called. 
n this case, it simply prints out some messages.

The decorator is applied to the say_hello function using the @my_decorator syntax. 
This is equivalent to calling say_hello and passing it as an argument to my_decorator, like this:

say_hello = my_decorator(say_hello)

When say_hello is called, the decorated version of the function is executed, which first prints "Before the function is called.", then calls the original function say_hello (which prints "Hello!"), and finally prints "After the function is called."
'''

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

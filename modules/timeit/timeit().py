'https://www.techgeekbuzz.com/python-timeit-with-examples/'


'https://docs.python.org/3/library/timeit.html'


'''
timeit.timeit(stmt, setup, timer, number)

timeit() is a method of Python timeit module. And it returns the execution time of the code snippet in seconds.

The timeit() method accepts the Python code snippet in a string and execute it 1 million times. And return the total execution time, 
by executing the code snippet 1 million times. 1 million times is the default number of executions, you can also change it.
'''

# testing timeit module

import timeit

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# time for 500.000 calculations
my_time = timeit.timeit("factorial(6)", number = 500_000, globals = globals())
print(f'factorial(6) repeated 500_000 times = {my_time} seconds')


# Measuring the time of execution:
import time

def my_function():
    # Your function code here
    time.sleep(2)  # Simulating some time-consuming task

start_time = time.time()
my_function()
end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
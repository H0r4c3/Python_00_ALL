'https://docs.python.org/3/library/itertools.html#itertools.count'

'''
Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers. Roughly equivalent to:

def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
        
Syntax: itertools.count(start=0, step=1)

Parameters:
start: Start of the sequence (defaults to 0)
step: Difference between consecutive numbers (defaults to 1)

Returns: Returns a count object whose .__next__() method returns consecutive values.
'''

from itertools import count
my_iterator = count(start = 1, step = 10)
print((next(my_iterator)))
print((next(my_iterator)))
print((next(my_iterator)))




'https://www.geeksforgeeks.org/python-itertools-count/'

# Example #1: Creating evenly spaced list of numbers
# itertools.count() can be used to generate infinite recursive sequences easily. Lets have a look

# Program for creating a list of even and odd list of integers using count()
from itertools import count
  
# creates a count iterator object
iterator = count(start = 0, step = 2)
  
# prints a odd list of integers
print("Even list:", list(next(iterator) for _ in range(5)))
  
# creates a count iterator object
iterator = (count(start = 1, step = 2))
  
# prints a odd list of integers
print("Odd list:", list(next(iterator) for _ in range(5)))



# Example #2: Emulating enumerate() using itertools.count()
# Program to emulate enumerate() using count()

my_list =["Geeks", "for", "Geeks"]
  
# count spits out integers for each value in my list
for i in zip(count(start = 1, step = 1), my_list):
      
    # prints tuple in an enumerated format
    print(i)

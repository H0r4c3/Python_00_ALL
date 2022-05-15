'https://docs.python.org/3/library/functions.html#enumerate'

'''
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. 
The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and 
the values obtained from iterating over iterable.

Equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        
        
Syntax: 

enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is 
              to be started, by default it is 0
'''

my_list = ['one', 'two', 'three', 'four']
print(list(enumerate(my_list)))


my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(list(enumerate((my_list), 5)))
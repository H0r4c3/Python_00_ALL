'https://docs.python.org/3/library/itertools.html#itertools.starmap'
'https://www.geeksforgeeks.org/python-itertools-starmap/'

'''
itertools.starmap(function, iterable)

Make an iterator that computes the function using arguments obtained from the iterable. 
Used instead of map() when argument parameters are already grouped in tuples from a single iterable (the data has been “pre-zipped”). 
The difference between map() and starmap() parallels the distinction between function(a,b) and function(*c).

def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
        
        
When an iterable is contained within another iterable and certain function has to be applied on them, starmap() is used. 
The starmap() considers each element of the iterable within another iterable as a separate item. It is similar to map().

'''

from itertools import starmap

# Example
my_list =[(2, 5), (3, 2), (4, 3)]
new_list = list(starmap(pow, my_list))
print(new_list) # -> [32, 9, 64]



# Difference between map() and starmap():

# map()
my_list =[2, 3, 4, 5, 6, 7]
ans = list(map(lambda x : x + 2, my_list))
print(ans) # -> [4, 5, 6, 7, 8, 9]

# starmap() (What if we want to add different numbers to different elements of the list ?!)
my_list =[(2, 3), (3, 1), (4, 6), (5, 3), (6, 5), (7, 2)]
ans = list(starmap(lambda x, y : x + y, my_list))
print(ans) # -> [5, 4, 10, 8, 11, 9]
'https://docs.python.org/3/library/itertools.html#itertools.cycle'

'''
Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, 
return elements from the saved copy. Repeats indefinitely. Roughly equivalent to:

def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
              
Note, this member of the toolkit may require significant auxiliary storage (depending on the length of the iterable).


This method prints all the values that are given as an argument to this method. 
And again it starts from the beginning when it reaches the end. To terminate this we need to keep a termination condition.
'''

# import itertools
# x=itertools.cycle([1,2,3])
# for i in x:
#     print(i)
    

from itertools import cycle

c = 0
l=['code', 'speedy']
for i in cycle(l):
    print(i, end='-')
    c+=1
    if(c > 10):
        break


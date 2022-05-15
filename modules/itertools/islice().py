'https://www.geeksforgeeks.org/python-itertools-islice/'

'''
islice() function
This iterator selectively prints the values mentioned in its iterable container passed as an argument.

Syntax:
islice(iterable, start, stop, step)

Itertools 'islice' method returns an iterator!!!!!!!!

Make an iterator that returns selected elements from the iterable. 
If start is non-zero, then elements from the iterable are skipped until start is reached. 
Afterward, elements are returned consecutively unless step is set higher than one which results in items being skipped. 
If stop is None, then iteration continues until the iterator is exhausted, if at all; 
otherwise, it stops at the specified position. Unlike regular slicing, islice() does not support negative values for start, stop, or step. 
Can be used to extract related fields from data where the internal structure has been flattened (for example, a multi-line report 
may list a name field on every third line).
'''

from itertools import islice

print(list(islice('ABCDEFG', 2))) # --> ['A', 'B']
print(islice('ABCDEFG', 2, 4)) # --> C D
print(islice('ABCDEFG', 2, None)) # --> C D E F G
print(islice('ABCDEFG', 0, None, 2)) # --> A C E G

result = list(islice(range(20), 5))
print(result) # -> [0, 1, 2, 3, 4]

li = [2, 4, 5, 7, 8, 10, 20] 
print(list(islice(li, 1, 6, 2))) # -> [4, 7, 10]

iterator_obj = islice(li, 1, 6, 2)
for item in iterator_obj:
    print(item)


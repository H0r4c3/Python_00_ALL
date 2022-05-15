'https://www.geeksforgeeks.org/python-itertools-zip_longest/'
'https://blog.teclado.com/python-zip_longest/'

'''
This iterator falls under the category of Terminating Iterators. It prints the values of iterables alternatively in sequence. 
If one of the iterables is printed fully, the remaining values are filled by the values assigned to fillvalue parameter.

So how does zip_longest differ from plain old zip?
Well, when we use zip, zip will stop combining our iterables as soon as one of them runs out of elements. 
If the other iterables are longer, we just throw those excess items away.

Luckily, we have zip_longest here to save us.
In essence, any time zip_longest doesn't have a value to match to one of our iterable's elements, it will place this fillvalue there to plug the gaps.
'''




from itertools import zip_longest  

# 1. Example
# using zip_longest() to combine two iterables.  
print ("The combined values of iterables is  : ")  
print (*(zip_longest('GesoGes', 'ekfrek', fillvalue ='_' ))) 
#The combined values of iterables is  : 
#('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')


# 2. Example
x =[1, 2, 3, 4, 5, 6, 7]
y =[8, 9, 10]
z = list(zip_longest(x, y))
print(z)
# Output: [(1, 8), (2, 9), (3, 10), (4, None), (5, None), (6, None), (7, None)]


# 3. Example
l_1 = [1, 2, 3]
l_2 = [1, 2]
combinated = list(zip_longest(l_1, l_2, fillvalue="_"))
print(combinated)  # [(1, 1), (2, 2), (3, '_')]
'https://docs.python.org/3/library/itertools.html#itertools.takewhile'
'https://www.geeksforgeeks.org/python-itertools-takewhile/'

'''
Make an iterator that returns elements from the iterable as long as the predicate is true.

Syntax:

takewhile(predicate, iterable)
The predicate is either a built-in function or a user-defined function. It can be even lambda functions.

Equivalent to:
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
            
The function takewhile() takes a predicate and an iterable as arguments. The iterable is iterated to check each of its elements. 
If the elements on the specified predicate, evaluates to true, it is returned. Otherwise, the loop is terminated.
'''

from itertools import takewhile

# 1. Example:

# function to check whether number is even
def even_number(x):
     return (x % 2 == 0)
  
# iterable (list)
my_list =[2, 4, 8, 22, 33, 6, 67]
  
new_list = list(takewhile(even_number, my_list))
print(new_list)


# 2. Example (using lambda)
my_string ="GeeksforGeeks"
  
# consider elements until 's' is encountered
result = list(takewhile(lambda x : x != 's', my_string))
  
print(result)



# 3. Example

ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']
 
res = ''.join(c[0] for c in takewhile(lambda x : all(x[0] == y for y in x), zip(*ini_strlist)))
 
# Printing result
print("Resultant prefix", res)
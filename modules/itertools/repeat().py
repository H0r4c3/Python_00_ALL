'https://www.geeksforgeeks.org/python-itertools-repeat/'

'''
itertools.repeat() falls under the category of infinite iterators. In repeat() we give the data and give the number, how many times the data will be repeated. 
If we will not specify the number, it will repeat infinite times. 
In repeat(), the memory space is not created for every variable. Rather it creates only one variable and repeats the same variable.

Syntax: repeat(val, num)

Parameters:
val: The value to be printed.
num: If the optional keyword num is mentioned, then it repeatedly prints the passed value num number of times, 
otherwise prints the passed value infinite number of times.
'''

from itertools import repeat
 
 
# 1. Example

print (list(repeat(25, 4)))


# 2. Example

my_list = [1, 2, 3, 4, 5]
my_new_list = [x for item in my_list for x in repeat(item, 3)]
print(my_new_list)
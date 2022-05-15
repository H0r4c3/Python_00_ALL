'https://www.geeksforgeeks.org/python-map-function/?ref=leftbar-rightbar'

'''
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

map(function, iterable)
Parameters :

function : It is a function to which map passes each element of given iterable.
iterable : It is a iterable which is to be mapped.
'''

# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))



# Triple all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x*3, numbers)
print(list(result))



# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# map applied on two lists
def add_list(a,b):
    return a + b
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(add_list, list1, list2))
print(result)
'https://www.geeksforgeeks.org/python-all-function/#:~:text=The%20all()%20function%20is,the%20iterable%20object%20is%20empty.'

'''
The all() function is an inbuilt function in Python which returns true if all the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True 
else it returns False. It also returns True if the iterable object is empty.

Syntax: all( iterable )
 
Parameters: Iterable: It is an iterable object such as a dictionary, tuple, list, set, etc.   
'''

# All elements of list are true
my_list = [4, 5, 1]
print(all(my_list))
 
# All elements of list are false
my_list = [0, 0, False]
print(all(my_list))
 
# Some elements of list are true, while others are false
my_list = [1, 0, 6, 7, False]
print(all(my_list))
 
# Empty List
my_list = []
print(all(my_list))


# All elements from a list are in another list
my_list1 = [1, 2, 3, 4]
my_list2 = [0, 1, 2, 3, 4, 5]
check =  all(item in my_list2 for item in my_list1)
print(check)


# All elements from a list are in another list
my_list1 = ['a', 'c', 'e']
my_list2 = ['a', 'b', 'c', 'd', 'e']
check =  all(item in my_list2 for item in my_list1)
print(check)
 
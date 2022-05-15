'https://www.geeksforgeeks.org/python-string-join-method/?ref=gcse'

'''
Python String join() method is a string method and returns a string in which the elements of the sequence have been joined by the str separator.

string_name.join(iterable)

Parameters: 

The join() method takes iterable – objects capable of returning their members one at a time. Some examples are List, Tuple, String, Dictionary, and Set

Return Value: 

The join() method returns a string concatenated with the elements of iterable. 

Type Error:

If the iterable contains any non-string values, it raises a TypeError exception. 
'''

list1 = ['1','2','3','4'] 
  
s = "-"
  
# joins elements of list1 by '-' and stores in sting s
s = s.join(list1)
  
# join use to join a list of strings to a separator s
print(s)


# Joining with empty separator
list1 = ['g','e','e','k', 's'] 
print("".join(list1))


# enclose Horace in parantheses
my_string = 'Horace'
result = my_string.join('()')
print(result)

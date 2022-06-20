'https://www.programiz.com/python-programming/methods/list/append'

'''
The syntax of the append() method is:

list.append(item)
append() Parameters
The method takes a single argument

item - an item (number, string, list etc.) to be added at the end of the list
Return Value from append()
The method doesn't return any value (returns None).
'''

#Example 1: Adding Element to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# Add 'guinea pig' to the list
animals.append('guinea pig')

print('Updated animals list: ', animals)


#Example 2: Adding List to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to animals
animals.append(wild_animals)

print('Updated animals list: ', animals)
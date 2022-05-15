'''
The remove() method removes the first matching element (which is passed as an argument) from the list.

list.remove(element)

The remove() method takes a single element as an argument and removes it from the list.
If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
'''

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig', 'rabbit', 'dog']

#the first 'dog' is removed
#animals.remove('dog')


# Updated animals List
print('Updated animals list: ', animals)


# ERROR: Deletes the first 'rabbit', not the second one!!!!!!!!!!!!!!
animals.remove(animals[4])
print(animals)
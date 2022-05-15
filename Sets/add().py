'https://www.geeksforgeeks.org/set-add-python/'

'''
set.add(elem)

The add() method doesn't add an element to the set if it's already present in it otherwise it will get added to the set.

Parameters:
add() takes single parameter(elem) which needs to be added in the set.

Returns:
The add() method doesn't return any value.
'''

# set of letters
my_set = {'g', 'e', 'k'}
  
# adding 's'
my_set.add('s')
print('Letters are:', my_set)
  
# adding 's' again
my_set.add('s')
print('Letters are:', my_set)
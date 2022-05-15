'https://www.tutorialsteacher.com/python/set-isdisjoint'

'''
The set.isdisjoint() method returns true if the given sets have no common elements. 
Sets are disjoint if and only if their intersection is the empty set.

set1.isdisjoint(set2)

set2 = The set to checked for being a disjoint set with set1.
Returns True if the sets are disjoin. False if the sets are not disjoint.
'''

nums = {1, 2, 3, 4, 5 }
oddNums = {1, 3, 5, 7, 9}
primeNums = {7, 11, 13}

print(nums.isdisjoint(oddNums))
print(nums.isdisjoint(primeNums))




'''The set.isdisjoint() method can take other iterable types as an argument such as list, string, dictionary, and tuple.'''

char_set = {'a','b','c','d','e'}
char_list = ['b','c','d']
char_str = 'ghij'
char_dict = {'a':1,'b':2}
char_tuple = ('x', 'y', 'z')

print(char_set.isdisjoint(char_list))
print(char_set.isdisjoint(char_str))
print(char_set.isdisjoint(char_dict))
print(char_set.isdisjoint(char_tuple))
'https://www.geeksforgeeks.org/itertools-groupby-in-python/'
'https://www.codespeedy.com/itertools-groupby-in-python/'

'''
This method calculates the keys for each element present in iterable. It returns key and iterable of grouped items.

Syntax: itertools.groupby(iterable, key_func)

Parameters:
iterable: Iterable can be of any kind (list, tuple, dictionary).
key: A function that calculates keys for each element present in iterable.

Return type: 
It returns consecutive keys and groups from the iterable. 
If the key function is not specified or is None, key defaults to an identity function and returns the element unchanged.

Features

A. Group consecutive items together
B. Group all occurrences of an item, given a sorted iterable
C. Specify how to group items with a key function *
'''

from itertools import groupby

s = "aa1abb2bcc3ccd"
x = groupby(s)
for k, g in x:
    print(k, list(g))
    
my_dict = {k: list(g) for k, g in groupby(s)}

print(my_dict)


#remove all consecutive duplicates of a given string
def remove_all_consecutive(str1): 
	result_str = [] 
	for (key, group) in groupby(str1): 
		result_str.append(key) 

	return ''.join(result_str)
	
str1 = 'xxxxxyyyyyxxxyyyy'
print("Original string:", str1)
print("After removing consecutive duplicates: ", remove_all_consecutive(str1))



things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
	for thing in group:
		print(key, thing[1])
	print("")
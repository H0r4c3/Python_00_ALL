'https://realpython.com/python-defaultdict/'

'''
A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and 
provides the default value for a nonexistent key.

A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

d.get(key, default) won't ever modify your dictionary – it will just return the default and leave the dictionary unchanged. 
defaultdict, on the other hand, will insert a key into the dictionary if it isn't there yet. This is a big difference; 
'''

from collections import defaultdict

# Correct instantiation
def_dict = defaultdict(list)  # Pass list to .default_factory
def_dict['one'] = 1  # Add a key-value pair
print(def_dict['missing'])  # Access a missing key returns an empty list
#[]
def_dict['another_missing'].append(4)  # Modify a missing key
print(def_dict)
#defaultdict(<class 'list'>, {'one': 1, 'missing': [], 'another_missing': [4]})
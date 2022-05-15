'https://www.geeksforgeeks.org/ordereddict-in-python/'

'''
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. 
The only difference between dict() and OrderedDict() is that:

OrderedDict preserves the order in which the keys are inserted.

Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.

Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion.

Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.
Ordered Dict can be used as a stack with the help of popitem function. Try implementing LRU cache with Ordered Dict.
'''

# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict
 
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
 
for key, value in d.items():
    print(key, value)
 
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)
    
    
# Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict
 
print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
 
print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)
    
    
# Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion.
# A Python program to demonstrate working of deletion
# re-insertion in OrderedDict
from collections import OrderedDict
 
print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)
 
print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)
 
print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)
    

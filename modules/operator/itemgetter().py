'https://docs.python.org/3/library/operator.html#operator.itemgetter'

'''
operator.itemgetter(*items)
Return a callable object that fetches item from its operand using the operand’s __getitem__() method. 
If multiple items are specified, returns a tuple of lookup values. For example:

After f = itemgetter(2), the call f(r) returns r[2].

After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
'''

from operator import itemgetter

# 1. Example
result = itemgetter(1, 3, 5)('ABCDEFG')
print(result) # -> ('B', 'D', 'F')



# 2. Example
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
print(list(map(itemgetter(1), inventory))) # -> [3, 2, 5, 1]
print(sorted(inventory, key=itemgetter(1))) # -> [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
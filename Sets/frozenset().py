'https://www.programiz.com/python-programming/methods/built-in/frozenset'

'''
The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.

Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain 
the same after creation.

Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).

The syntax of frozenset() function is:

frozenset([iterable])
frozenset() Parameters
The frozenset() function takes a single parameter:

iterable (Optional) - the iterable which contains elements to initialize the frozenset with.
Iterable can be set, dictionary, tuple, etc.

Return value from frozenset()
The frozenset() function returns an immutable frozenset initialized with elements from the given iterable.

If no parameters are passed, it returns an empty frozenset.
'''

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
fSet.add('v')
'The isinstance() function returns True if the specified object is of the specified type, otherwise False.'
'isinstance(object, type)'
'isinstance(object, tuple of types)'

print(isinstance(5, int))
print(isinstance([1, 2, 3], list))

print(isinstance(5, (int, float, list)))

print(isinstance("Hello", (float, int, str, list, dict, tuple)))

'https://www.programiz.com/python-programming/methods/string/splitlines'

'''
The splitlines() method splits the string at line breaks and returns a list of lines in the string.

The syntax of splitlines() is:

str.splitlines([keepends])

splitlines() takes maximum of 1 parameter.
keepends (optional) - If keepends is provided and True, line breaks are also included in items of the list.
By default, the line breaks are not included.

Return Value from splitlines()
splitlines() returns a list of lines in the string.

If there are not line break characters, it returns a list with a single item (a single line).
'''

grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())
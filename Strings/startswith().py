'https://www.programiz.com/python-programming/methods/string/startswith'

'''
The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.

The syntax of startswith() is:

str.startswith(prefix[, start[, end]])

Parameters:
startswith() method takes a maximum of three parameters:

prefix - String or tuple of strings to be checked
start (optional) - Beginning position where prefix is to be checked within the string.
end (optional) - Ending position where prefix is to be checked within the string.

Return Value:
startswith() method returns a boolean.

It returns True if the string starts with the specified prefix.
It returns False if the string doesn't start with the specified prefix.
'''

text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)
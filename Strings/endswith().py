'https://www.programiz.com/python-programming/methods/string/endswith'

'''
The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

str.endswith(suffix[, start[, end]])

The endswith() takes three parameters:

suffix - String or tuple of suffixes to be checked
start (optional) - Beginning position where suffix is to be checked within the string.
end (optional) - Ending position where suffix is to be checked within the string.

The endswith() method returns a boolean.

It returns True if a string ends with the specified suffix.
It returns False if a string doesn't end with the specified suffix.
'''

# Example 1: endswith() Without start and end Parameters

text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)


# Example 2: endswith() With start and end Parameters

text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)


# Example 3: endswith() With Tuple Suffix

text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result)